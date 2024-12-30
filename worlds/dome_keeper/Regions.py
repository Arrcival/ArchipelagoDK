from typing import NamedTuple, Optional, List, Dict, TYPE_CHECKING
from BaseClasses import Location, LocationProgressType, Region
from worlds.dome_keeper.Options import ProgressionType
from .Locations import (
    DomeKeeperLocationData,
    generate_caves_locations, 
    generate_switches_location_for_layer, 
    location_table_easy_upgrades, 
    location_table_hard_upgrades,
    location_table_normal_upgrades,
    location_assignments_challenge,
    location_assignments_regular
)
from .Items import generate_item, item_assignments

if TYPE_CHECKING:
    from . import DomeKeeperWorld

GUILD_ASSIGNMENT_NAMES = [
    "Showdown",
    "Iron contribution",
    "Upside down",
    "Maze",
    "Projectile hell",
    "Dense iron",
    "Barren lands",
    "Defective weapon",
    "Heavy hitters",
    "Swiss cheese",
    "Logistical problem",
    "High risk",
    "Monster masses ",
    "Iron shortage",
    "Mining problem",
    "Cobalt contribution"
]


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

    menuRegion = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menuRegion)

    if (world.options.progression_type == ProgressionType.option_Relic_Hunt_Progression_Layers
     or world.options.progression_type == ProgressionType.option_Relic_Hunt_No_Progression):
        create_every_regions_relic_hunt(world)
        # link up our region with the entrance we just made
        menuRegion.connect(world.multiworld.get_region('Layer 1', world.player))
    
    if world.options.progression_type == ProgressionType.option_Guild_Assignments:
        create_every_regions_guild_assignments(world)
    

    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(
        world.goalItems, world.player
    )

# player >= 2
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

        menu_region.connect(region)
        world.multiworld.regions.append(region)

def create_every_regions_relic_hunt(world: "DomeKeeperWorld"):
    caves_location: list[DomeKeeperLocationData] = generate_caves_locations()
    switchesPerLayer = world.switchesPerLayer

    layerNumber = 1
    for switches in switchesPerLayer:
        region = Region("Layer " + str(layerNumber), world.player, world.multiworld)

        # layerNumber - 1 cause I want the index layer
        # [:switches] because I want only the x first switches for that layer

        switches_locations = generate_switches_location_for_layer(layerNumber - 1)
        switches_locations_cropped = switches_locations[:switches]

        region.locations.extend(map_locations(switches_locations_cropped, world, region, LocationProgressType.DEFAULT))

        current_cave: DomeKeeperLocationData = caves_location.pop(0)

        cave_location: DomeKeeperLocation = map_location(current_cave, world, region)
        cave_location.progress_type = LocationProgressType.PRIORITY
        region.locations.append(cave_location)

        if layerNumber == 1:
            region.locations.extend(map_locations(location_table_easy_upgrades, world, region, LocationProgressType.DEFAULT))
        if layerNumber == 2:
            region.locations.extend(map_locations(location_table_normal_upgrades, world, region, LocationProgressType.DEFAULT))
        if layerNumber == 3:
            region.locations.extend(map_locations(location_table_hard_upgrades, world, region, LocationProgressType.DEFAULT))
        
        world.multiworld.regions.append(region)
        if layerNumber >= 2:
            world.multiworld.get_region('Layer ' + str(layerNumber - 1), world.player).connect(region)

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
