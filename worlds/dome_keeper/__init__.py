import math
import string
from BaseClasses import Item, ItemClassification, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.dome_keeper.Rules import set_rules_colored_layers
from .Items import (
    ItemDataCode,
    generate_all_items,
    items_engineer,
    items_assessor,
    items_laser,
    items_sword,
    items_artillery,
    items_tesla,
    items_shield,
    items_orchard,
    items_repellent,
    item_trap_wavestart,
    item_filler_cobalt,
    item_layer_unlock,
    item_engineer_drill,
    item_assessor_spheres_strength,
    item_assessor_spheres_lifetime,
    items_droneyard,
    item_droneyard_drones
)
from .Options import Dome, DomeKeeperOptions, Keeper, DomeGadget
from .Option_Groups import dk_option_groups
from .Locations import UPGRADES_LOCATIONS_AMOUNT, generate_locations_data
from .Regions import create_every_regions
from .Presets import dk_options_presets


AP_VERSION = "1.0.0"


class DomeKeeperItem(Item):
    game = "Dome Keeper"

    def __init__(self, code, name, classification: ItemClassification, player: int = None):
        super(DomeKeeperItem, self).__init__(
            name,
            classification,
            code,
            player
        )


class DomeKeeperWeb(WebWorld):
    options_presets = dk_options_presets
    option_groups = dk_option_groups
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Dome Keeper for Archipelago."
        "",
        "English",
        "dome_keeper_en.md",
        "dome_keeper/en",
        ["Arrcival"]
    )]

class DomeKeeperWorld(World):
    """Dome Keeper is a roguelike/mining game where you need to dig up a relic while defending waves of enemies."""

    game = "Dome Keeper"  # name of the game/world
    options_dataclass = DomeKeeperOptions
    options: DomeKeeperOptions
    item_name_to_id = {data.name: id for id, data in generate_all_items().items()}
    location_name_to_id = {location.name: location.code for location in generate_locations_data()}
    topology_present = True
    web = DomeKeeperWeb()
    required_client_version = (0, 5, 1)

    base_id = 4242001

    pool: list[Item] = []
    itempoolcount = 0
    switchesPerLayer: list[int] = []
    goalItems: list[str] = []
        
    def set_rules(self):
        set_rules_colored_layers(self, self.player)

    def generate_early(self):
        if self.options.keeper == Keeper.option_Engineer:
            self.itempoolcount += 8
            self.itempoolcount += self.options.drill_upgrades.value
        if self.options.keeper == Keeper.option_Assessor:
            self.itempoolcount += 18
            self.itempoolcount += self.options.kinetic_spheres.value
            self.itempoolcount += self.options.sphere_lifetime.value

        if self.options.dome == Dome.option_Laser:
            self.itempoolcount += 9
        if self.options.dome == Dome.option_Sword:
            self.itempoolcount += 14
        if self.options.dome == Dome.option_Artillery:
            self.itempoolcount += 10
        if self.options.dome == Dome.option_Tesla:
            self.itempoolcount += 20
        
        if self.options.dome_gadget == DomeGadget.option_Repellent:
            self.itempoolcount += 11
        if self.options.dome_gadget == DomeGadget.option_Shield:
            self.itempoolcount += 9
        if self.options.dome_gadget == DomeGadget.option_Orchard:
            self.itempoolcount += 14
        if self.options.dome_gadget == DomeGadget.option_Droneyard:
            self.itempoolcount += 11
            self.itempoolcount += self.options.droneyard_drones.value

        self.itempoolcount += self.options.extra_cobalt.value

        # progression items to unlock layers
        if self.options.colored_layers.value:
            goalItems = [item.name for item in generate_progression_items(self.player, self.options.map_size.value)]
            self.itempoolcount += len(goalItems)

            self.goalItems += goalItems
        
        layers_amount = getLayersAmountBasedOnMapSize(self.options.map_size.value)
        # amount of items minus upgrades minus caves (which is the amount of layers)
        self.switchesPerLayer = generateSwitchesPerLayer(self.itempoolcount - UPGRADES_LOCATIONS_AMOUNT - layers_amount, self.options.map_size.value)
        

    def create_items(self):
        self.pool.clear()
        if self.options.keeper == Keeper.option_Engineer:
            self.pool += generate_items(items_engineer, self.player)
            self.pool += generate_item(item_engineer_drill, self.player, self.options.drill_upgrades.value)
        if self.options.keeper == Keeper.option_Assessor:
            self.pool += generate_items(items_assessor, self.player)
            self.pool += generate_item(item_assessor_spheres_strength, self.player, self.options.kinetic_spheres.value)
            self.pool += generate_item(item_assessor_spheres_lifetime, self.player, self.options.sphere_lifetime.value)

        if self.options.dome == Dome.option_Laser:
            self.pool += generate_items(items_laser, self.player)
        if self.options.dome == Dome.option_Sword:
            self.pool += generate_items(items_sword, self.player)
        if self.options.dome == Dome.option_Artillery:
            self.pool += generate_items(items_artillery, self.player)
        if self.options.dome == Dome.option_Tesla:
            self.pool += generate_items(items_tesla, self.player)
        
        if self.options.dome_gadget == DomeGadget.option_Orchard:
            self.pool += generate_items(items_orchard, self.player)
        if self.options.dome_gadget == DomeGadget.option_Repellent:
            self.pool += generate_items(items_repellent, self.player)
        if self.options.dome_gadget == DomeGadget.option_Shield:
            self.pool += generate_items(items_shield, self.player)
        if self.options.dome_gadget == DomeGadget.option_Droneyard:
            self.pool += generate_items(items_droneyard, self.player)
            self.pool += generate_item(item_droneyard_drones, self.player, self.options.droneyard_drones.value)

        if self.options.colored_layers.value:
            self.pool += generate_progression_items(self.player, self.options.map_size.value)

        self.pool += generate_junk_cobalts(self.player, self.options.extra_cobalt.value)

        self.multiworld.itempool += self.pool


    def create_item(self, name: str) -> Item:
        return DomeKeeperItem(name, self.player, ItemClassification.filler)
        
    def create_regions(self):
        create_every_regions(self)

    def fill_slot_data(self) -> dict:
        return {
            "seed": "".join(self.random.choice(string.digits) for _ in range(8)),
            "keeper": self.options.keeper.value,
            "dome": self.options.dome.value,
            "domeGadget": self.options.dome_gadget.value,
            "mapSize": self.options.map_size.value,
            "difficulty": self.options.difficulty.value,
            "deathLink": self.options.death_link.value,
            "switchesPerLayers": self.switchesPerLayer,
            "drillUpgrades": self.options.drill_upgrades.value,
            "kineticSpheres": self.options.kinetic_spheres.value,
            "sphereLifetime": self.options.sphere_lifetime.value,
            "dronesAmount": self.options.droneyard_drones.value,
            "coloredLayersProgression": self.options.colored_layers.value,
            "miningEverything": self.options.mining_everything.value
        }

def generate_item(itemDataCode: ItemDataCode, player, amount) -> list[DomeKeeperItem]:
    values = []
    for _ in range(amount):
        values.append(DomeKeeperItem(itemDataCode.code, itemDataCode.data.name, itemDataCode.data.classification, player))
    return values


def generate_items(itemDataCodes: list[ItemDataCode], player) -> list[DomeKeeperItem]:
    values = []
    for itemDataCode in itemDataCodes:
        for _ in range(itemDataCode.data.count):
            values.append(DomeKeeperItem(itemDataCode.code, itemDataCode.data.name, itemDataCode.data.classification, player))
    return values

def generate_progression_items(player: int, mapSize: int):
    values: list[DomeKeeperItem] = []
    layers = getProgressionLayersAmount(mapSize)
    for _ in range(layers):
        values.append(DomeKeeperItem(item_layer_unlock.code, item_layer_unlock.data.name, item_layer_unlock.data.classification, player))
    return values

def generate_junk_cobalts(player, amount):
    # edit later for traps
    values = []
    for _ in range(amount):
        values.append(DomeKeeperItem(item_filler_cobalt.code, item_filler_cobalt.data.name, item_filler_cobalt.data.classification, player))
    return values

def generateSwitchesPerLayer(switchesAmount: int, mapSize: int) -> list[int]:
    # Small : 3, medium : 4, large : 6, huge: 7
    layers = getLayersAmountBasedOnMapSize(mapSize)
    
    # Splits evenly switches per layers avaible
    max_value = math.floor(switchesAmount / layers)
    remaining = switchesAmount % layers
    result = [max_value] * layers
    for i in range(remaining):
        result[i] += 1

    return result

def getProgressionLayersAmount(mapSize: int) -> int:
    return getLayersAmountBasedOnMapSize(mapSize) - 1 

def getLayersAmountBasedOnMapSize(mapSize: int) -> int:
    # Small is 0 : 3 layers
    # Medium is 1 : 4 layers
    # Large is 2 : 6 layers
    # Huge is 3 : 7 layers
    layers = mapSize + 3
    if mapSize >= 2:
        layers += 1
    return layers