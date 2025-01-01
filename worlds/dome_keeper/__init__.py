import math
import string
from BaseClasses import Item, ItemClassification, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.dome_keeper.Rules import get_unlocks_without_starting, set_every_rules
from .Items import (
    all_items,
    generate_engineer_upgrades,
    generate_assessor_upgrades,
    generate_item,
    generate_laser_upgrades,
    generate_sword_upgrades,
    generate_artillery_upgrades,
    generate_tesla_upgrades,
    generate_repellent_upgrades,
    generate_shield_upgrades,
    generate_orchard_upgrades,
    generate_droneyard_upgrades,
    generate_layers_upgrades,
    generate_cobalt_upgrades,
    generate_iron_rewards,
    generate_water_rewards,
    generate_cobalt_rewards,
    item_filler_cobalt
)
from .Options import Dome, DomeKeeperOptions, Keeper, DomeGadget, ProgressionType
from .Option_Groups import dk_option_groups
from .Locations import UPGRADES_LOCATIONS_AMOUNT, generate_locations_data
from .Regions import create_every_regions
from .Presets import dk_options_presets


AP_VERSION = "1.1.0"

TOTAL_RESSOURCES_GA = 17

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
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Dome Keeper for Archipelago.",
        "English",
        "dome_keeper_en.md",
        "dome_keeper/en",
        ["Arrcival"]
    )

    tutorials = [setup_en]

class DomeKeeperWorld(World):
    """Dome Keeper is a roguelike/mining game where you need to dig up a relic while defending waves of enemies."""

    game = "Dome Keeper"  # name of the game/world
    options_dataclass = DomeKeeperOptions
    options: DomeKeeperOptions
    item_name_to_id = {itemDataCode.name: itemDataCode.code for itemDataCode in all_items}
    location_name_to_id = {location.name: location.code for location in generate_locations_data()}
    topology_present = True
    web = DomeKeeperWeb()
    required_client_version = (0, 5, 1)

    base_id = 4242000

    pool: list[Item] = []
    itempoolcount = 0
    switchesPerLayer: list[int] = []
    goalItems: list[str] = []

    ga_final_assignment: int
        
    def set_rules(self):
        set_every_rules(self, self.player)

    def generate_early(self):
        if self.options.progression_type == ProgressionType.option_Guild_Assignments:
            self.itempoolcount += 32

            unlocks: list[Item] = get_unlocks_without_starting(self.player, self.options.first_assignment.value)
            self.goalItems += [item.name for item in unlocks]

            self.ga_final_assignment = self.random.randint(0, 14)
            return

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
        if self.options.progression_type == ProgressionType.option_Relic_Hunt_Progression_Layers:
            layers_unlock_amount = getProgressionLayersAmount(self.options.map_size.value)
            goalItems = [item.name for item in generate_layers_upgrades(self.player, layers_unlock_amount)]
            self.itempoolcount += len(goalItems)

            self.goalItems += goalItems
        
        layers_amount = getLayersAmountBasedOnMapSize(self.options.map_size.value)
        # amount of items minus upgrades minus caves (which is the amount of layers)
        self.switchesPerLayer = generateSwitchesPerLayer(self.itempoolcount - UPGRADES_LOCATIONS_AMOUNT - layers_amount, self.options.map_size.value)

    def create_items(self):
        self.pool.clear()

        # Async items
        if self.options.progression_type == ProgressionType.option_Guild_Assignments:
            unlocks = get_unlocks_without_starting(self.player, self.options.first_assignment.value)
            self.pool += unlocks

            iron_amount = TOTAL_RESSOURCES_GA - self.options.starting_water.value - self.options.starting_cobalt.value
            self.pool += generate_iron_rewards(self.player, iron_amount)
            self.pool += generate_water_rewards(self.player, self.options.starting_water.value)
            self.pool += generate_cobalt_rewards(self.player, self.options.starting_cobalt.value)
            
            self.multiworld.itempool += self.pool
            return
        
        # Sync items
        if self.options.keeper == Keeper.option_Engineer:
            self.pool += generate_engineer_upgrades(self.player, self.options.drill_upgrades.value)
        if self.options.keeper == Keeper.option_Assessor:
            self.pool += generate_assessor_upgrades(self.player, self.options.kinetic_spheres.value, self.options.sphere_lifetime.value)

        if self.options.dome == Dome.option_Laser:
            self.pool += generate_laser_upgrades(self.player)
        if self.options.dome == Dome.option_Sword:
            self.pool += generate_sword_upgrades(self.player)
        if self.options.dome == Dome.option_Artillery:
            self.pool += generate_artillery_upgrades(self.player)
        if self.options.dome == Dome.option_Tesla:
            self.pool += generate_tesla_upgrades(self.player)
        
        if self.options.dome_gadget == DomeGadget.option_Orchard:
            self.pool += generate_orchard_upgrades(self.player)
        if self.options.dome_gadget == DomeGadget.option_Repellent:
            self.pool += generate_repellent_upgrades(self.player)
        if self.options.dome_gadget == DomeGadget.option_Shield:
            self.pool += generate_shield_upgrades(self.player)
        if self.options.dome_gadget == DomeGadget.option_Droneyard:
            self.pool += generate_droneyard_upgrades(self.player, self.options.droneyard_drones.value)

        if self.options.progression_type == ProgressionType.option_Relic_Hunt_Progression_Layers:
            layers_unlock_amount = getProgressionLayersAmount(self.options.map_size.value)
            self.pool += generate_layers_upgrades(self.player, layers_unlock_amount)

        self.pool += generate_cobalt_upgrades(self.player, self.options.extra_cobalt.value)

        self.multiworld.itempool += self.pool

    def create_item(self, name: str) -> Item:
        for item in all_items:
            if item.name == name:
                return generate_item(self.player, item)
        
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
            "progressionType": self.options.progression_type.value,
            "miningEverything": self.options.mining_everything.value,
            "assignmentsAmount": self.options.assignment_amount.value,
            "startingGA": self.options.first_assignment.value,
            "challengeMode": self.options.challenge_mode.value
        }

    def get_filler_item_name(self) -> str:
        return item_filler_cobalt.data.name

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