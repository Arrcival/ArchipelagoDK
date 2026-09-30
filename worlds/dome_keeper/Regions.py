from typing import NamedTuple, Optional, List, Dict, TYPE_CHECKING
from BaseClasses import Location, LocationProgressType, Region
from worlds.dome_keeper.Options import ProgressionType
from .Locations import (
    DomeKeeperLocationData,
    generate_caves_locations,
    generate_treasures_locations, 
    generate_switches_location_for_layer, 
    location_table_easy_upgrades, 
    location_table_hard_upgrades,
    location_table_normal_upgrades,
    location_assignments_challenge,
    location_assignments_regular,
    location_assignments_first_treasure,
    location_assignments_second_treasure,
    #location_assignments_third_treasure,
    get_layers_amount_from_map_size
)
from .Items import item_layer_unlock
from .Utils import layer_treasure_location_name, GUILD_ASSIGNMENT_NAMES, layer_region_name, assignment_entrance_name, layer_entrance_name

if TYPE_CHECKING:
    from . import DomeKeeperWorld


class DomeKeeperLocation(Location):
    game: str = "Dome Keeper"

    def __init__(self, world: "DomeKeeperWorld", name: str, code: int, region: Region, progress_type: LocationProgressType= LocationProgressType.DEFAULT):
        self.player = world.player
        self.name = name
        self.code = code
        self.parent_region = region
        self.progress_type = progress_type
        self.address = world.location_name_to_id[self.name]

class DomeKeeperRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

def create_every_regions(world: "DomeKeeperWorld"):
    menu_region = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menu_region)

    progression_type = world.options.progression_type.value

    create_regions(world, progression_type, menu_region)
    create_goal_items(world, progression_type)

def create_regions(world: "DomeKeeperWorld", progression_type: int, menu_region: Region):
    if progression_type in (
        ProgressionType.option_Relic_Hunt_Progression_Layers,
        ProgressionType.option_Relic_Hunt_No_Progression,
    ):
        create_every_regions_relic_hunt(world)
        menu_region.connect(world.multiworld.get_region(layer_region_name(1), world.player), layer_entrance_name(1))
    elif progression_type == ProgressionType.option_Guild_Assignments:
        create_every_regions_guild_assignments(world)

def create_goal_items(world: "DomeKeeperWorld", progression_type: int):
    if progression_type == ProgressionType.option_Guild_Assignments:
        # One assignment is available from the start, so only (assignment_amount - 1) unlocks are needed.
        required_unlocks = min(len(world.goal_items), max(0, world.options.assignment_amount.value - 1))
        world.multiworld.completion_condition[world.player] = (
            lambda state, required_unlocks=required_unlocks: state.has_from_list(world.goal_items, world.player, required_unlocks)
        )
    elif progression_type == ProgressionType.option_Relic_Hunt_Progression_Layers:
        required = len(world.goal_items)  # number of layer unlock items generated
        world.multiworld.completion_condition[world.player] = (
            lambda state, required=required: state.has(item_layer_unlock.name, world.player, required)
        )
    else:
        deepest = get_layers_amount_from_map_size(world.options.map_size.value)
        target = layer_treasure_location_name(deepest)
        world.multiworld.completion_condition[world.player] = (
            lambda state, target=target: state.can_reach_location(target, world.player)
        )

def create_every_regions_guild_assignments(world: "DomeKeeperWorld"):
    menu_region: Region = world.multiworld.get_region('Menu', world.player)

    progression_locations = []
    non_progression_locations = []
    if world.options.challenge_mode.value:
        progression_locations = location_assignments_challenge
        non_progression_locations = location_assignments_regular
    else:
        progression_locations = location_assignments_regular
        non_progression_locations = location_assignments_challenge

    for i in range(len(GUILD_ASSIGNMENT_NAMES)):
        region = Region(GUILD_ASSIGNMENT_NAMES[i], world.player, world.multiworld)

        region.locations.append(map_location(progression_locations[i], world, region, LocationProgressType.DEFAULT))
        region.locations.append(map_location(non_progression_locations[i], world, region, LocationProgressType.EXCLUDED))
        region.locations.append(map_location(location_assignments_first_treasure[i], world, region, LocationProgressType.DEFAULT))
        region.locations.append(map_location(location_assignments_second_treasure[i], world, region, LocationProgressType.DEFAULT))
        #region.locations.append(map_location(location_assignments_third_treasure[i], world, region, LocationProgressType.DEFAULT))

        menu_region.connect(region, assignment_entrance_name(i))
        world.multiworld.regions.append(region)

def create_every_regions_relic_hunt(world: "DomeKeeperWorld"):
    caves_location: list[DomeKeeperLocationData] = generate_caves_locations()
    charms_location: list[DomeKeeperLocationData] = generate_treasures_locations()
    switchesPerLayer = world.switches_per_layer

    layerNumber = 1
    for switches in switchesPerLayer:
        region = Region(layer_region_name(layerNumber), world.player, world.multiworld)

        # layerNumber - 1 cause I want the index layer
        # [:switches] because I want only the x first switches for that layer

        switches_locations = generate_switches_location_for_layer(layerNumber - 1)
        switches_locations_cropped = switches_locations[:switches]

        region.locations.extend(map_locations(switches_locations_cropped, world, region, LocationProgressType.DEFAULT))

        current_cave: DomeKeeperLocationData = caves_location.pop(0)
        current_charm: DomeKeeperLocationData = charms_location.pop(0)

        cave_location: DomeKeeperLocation = map_location(current_cave, world, region)
        region.locations.append(cave_location)

        charm_location: DomeKeeperLocation = map_location(current_charm, world, region)
        region.locations.append(charm_location)

        if layerNumber == 1:
            region.locations.extend(map_locations(location_table_easy_upgrades, world, region, LocationProgressType.DEFAULT))
        if layerNumber == 2:
            region.locations.extend(map_locations(location_table_normal_upgrades, world, region, LocationProgressType.DEFAULT))
        if layerNumber == 3:
            region.locations.extend(map_locations(location_table_hard_upgrades, world, region, LocationProgressType.DEFAULT))
        
        world.multiworld.regions.append(region)
        if layerNumber >= 2:
            previous = world.multiworld.get_region(layer_region_name(layerNumber - 1), world.player)
            previous.connect(region, layer_entrance_name(layerNumber))
        layerNumber += 1

def map_locations(locations: list[DomeKeeperLocationData],
                  world: "DomeKeeperWorld",
                  region: Region, 
                  progress_type: LocationProgressType= LocationProgressType.DEFAULT) -> list[DomeKeeperLocation]:
    return [DomeKeeperLocation(world, location.name, location.code, region, progress_type) for location in locations]

def map_location(location: DomeKeeperLocationData,
                 world: "DomeKeeperWorld", 
                 region: Region, 
                 progress_type: LocationProgressType= LocationProgressType.DEFAULT) -> DomeKeeperLocation:
    return DomeKeeperLocation(world, location.name, location.code, region, progress_type)
