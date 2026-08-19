import math
import string
from BaseClasses import Item, MultiWorld, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.dome_keeper.Rules import get_unlocks_without_starting, set_every_rules
from .Items import (
    all_items,
    generate_engineer_upgrades,
    generate_assessor_upgrades,
    generate_infiltrator_upgrades,
    generate_beastmaster_upgrades,
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
    generate_iron_upgrades,
    generate_traps,
    generate_water_upgrades,
    generate_cobalt_upgrades,
    generate_iron_rewards,
    generate_water_rewards,
    generate_cobalt_rewards,
    item_filler_iron,
    ItemDataCode
)
from .Options import Dome, DomeKeeperOptions, Keeper, DomeGadget, ProgressionType, HaveDLC
from .Option_Groups import dk_option_groups
from .Locations import generate_locations_data, get_layers_amount_from_map_size, get_non_switch_location_count
from .Regions import create_every_regions
from .Presets import dk_options_presets


AP_VERSION = "2.0.0"

TOTAL_RESOURCES_GA = 49

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
    required_client_version = (0, 6, 8)

    base_id = 4242000

    items_by_name: dict[str, ItemDataCode]
    switches_per_layer: list[int]
    goal_items: list[str]

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.items_by_name = {item.name: item for item in all_items}
        self.switches_per_layer = []
        self.goal_items = []

    def set_rules(self):
        set_every_rules(self, self.player)


    def generate_early(self):
        if self.options.progression_type.value == ProgressionType.option_Guild_Assignments:

            unlocks: list[Item] = get_unlocks_without_starting(self.player, self.options.first_assignment.value)
            self.goal_items += [item.name for item in unlocks]
            return

        # progression items to unlock layers
        if self.options.progression_type.value == ProgressionType.option_Relic_Hunt_Progression_Layers:
            layers_unlock_amount = get_progression_layers_amount(self.options.map_size.value)
            self.goal_items += [item.name for item in generate_layers_upgrades(self.player, layers_unlock_amount)]

        item_count = len(self._build_item_pool())
        non_switch_location_count = get_non_switch_location_count(self.options.map_size.value)

        switches_amount = max(0, item_count - non_switch_location_count)
        self.switches_per_layer = generate_switches_per_layer(switches_amount, self.options.map_size.value)

    def _build_item_pool(self) -> list[Item]:
        pool: list[Item] = []
        pool += generate_traps(self.player, self.options.trap_wave.value)

        # Async items
        if self.options.progression_type.value == ProgressionType.option_Guild_Assignments:
            unlocks = get_unlocks_without_starting(self.player, self.options.first_assignment.value)
            pool += unlocks

            iron_amount = TOTAL_RESOURCES_GA - self.options.starting_water.value - self.options.starting_cobalt.value - self.options.trap_wave.value
            pool += generate_iron_rewards(self.player, iron_amount)
            pool += generate_water_rewards(self.player, self.options.starting_water.value)
            pool += generate_cobalt_rewards(self.player, self.options.starting_cobalt.value)
            return pool

        # Sync items
        keeper_value = self.options.keeper.value
        if keeper_value == Keeper.option_Infiltrator or keeper_value == Keeper.option_Beastmaster:
            if self.options.have_dlc.value == HaveDLC.option_false:
                keeper_value = Keeper.option_Engineer if keeper_value == Keeper.option_Infiltrator else Keeper.option_Assessor

        if keeper_value == Keeper.option_Engineer:
            pool += generate_engineer_upgrades(self.player, self.options.drill_upgrades.value)
        if keeper_value == Keeper.option_Assessor:
            pool += generate_assessor_upgrades(self.player, self.options.kinetic_spheres.value, self.options.sphere_lifetime.value)
        if keeper_value == Keeper.option_Infiltrator:
            pool += generate_infiltrator_upgrades(self.player, self.options.kunai_upgrades.value)
        if keeper_value == Keeper.option_Beastmaster:
            pool += generate_beastmaster_upgrades(self.player, self.options.catgoblins_amount.value)

        if self.options.dome.value == Dome.option_Laser:
            pool += generate_laser_upgrades(self.player)
        if self.options.dome.value == Dome.option_Sword:
            pool += generate_sword_upgrades(self.player)
        if self.options.dome.value == Dome.option_Artillery:
            pool += generate_artillery_upgrades(self.player)
        if self.options.dome.value == Dome.option_Tesla:
            pool += generate_tesla_upgrades(self.player)

        if self.options.dome_gadget.value == DomeGadget.option_Orchard:
            pool += generate_orchard_upgrades(self.player)
        if self.options.dome_gadget.value == DomeGadget.option_Repellent:
            pool += generate_repellent_upgrades(self.player)
        if self.options.dome_gadget.value == DomeGadget.option_Shield:
            pool += generate_shield_upgrades(self.player)
        if self.options.dome_gadget.value == DomeGadget.option_Droneyard:
            pool += generate_droneyard_upgrades(self.player, self.options.droneyard_drones.value)

        if self.options.progression_type.value == ProgressionType.option_Relic_Hunt_Progression_Layers:
            layers_unlock_amount = get_progression_layers_amount(self.options.map_size.value)
            pool += generate_layers_upgrades(self.player, layers_unlock_amount)

        pool += generate_cobalt_upgrades(self.player, self.options.extra_cobalt.value)
        pool += generate_water_upgrades(self.player, self.options.extra_water.value)
        pool += generate_iron_upgrades(self.player, self.options.extra_iron.value)
        return pool

    def create_items(self):
        self.multiworld.itempool += self._build_item_pool()

    def create_item(self, name: str) -> Item:
        item_data = self.items_by_name.get(name, item_filler_iron)
        return generate_item(self.player, item_data)
        
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
            "switchesPerLayer": self.switches_per_layer,
            "drillUpgrades": self.options.drill_upgrades.value,
            "kineticSpheres": self.options.kinetic_spheres.value,
            "sphereLifetime": self.options.sphere_lifetime.value,
            "kunaiUpgrades": self.options.kunai_upgrades.value,
            "catgoblinsAmount": self.options.catgoblins_amount.value,
            "dronesAmount": self.options.droneyard_drones.value,
            "progressionType": self.options.progression_type.value,
            "miningEverything": self.options.mining_everything.value,
            "assignmentsAmount": self.options.assignment_amount.value,
            "startingGA": self.options.first_assignment.value,
            "challengeMode": self.options.challenge_mode.value
        }

    def get_filler_item_name(self) -> str:
        return item_filler_iron.name

def generate_switches_per_layer(switchesAmount: int, mapSize: int) -> list[int]:
    # Small : 3, medium : 4, large : 6, huge: 7
    layers = get_layers_amount_from_map_size(mapSize)
    
    # Splits evenly switches per layers avaible
    max_value = math.floor(switchesAmount / layers)
    remaining = switchesAmount % layers
    result = [max_value] * layers
    for i in range(remaining):
        result[i] += 1

    return result

def get_progression_layers_amount(mapSize: int) -> int:
    return get_layers_amount_from_map_size(mapSize) - 1 

