from typing import NamedTuple, Optional, List, Dict, TYPE_CHECKING
from BaseClasses import Location, LocationProgressType, Region
from .Locations import (
    DomeKeeperLocationData,
    generate_caves_locations, 
    generate_switches_location_for_layer, 
    location_table_easy_upgrades, 
    location_table_hard_upgrades,
    location_table_normal_upgrades
)

if TYPE_CHECKING:
    from . import DomeKeeperWorld

class DomeKeeperRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

def create_every_regions(world: "DomeKeeperWorld"):

    menuRegion = Region("Menu", world.player, world.multiworld)
    world.multiworld.regions.append(menuRegion)

    caves_location: list[DomeKeeperLocationData] = generate_caves_locations()
    switchesPerLayer = world.switchesPerLayer

    layerNumber = 1
    for switches in switchesPerLayer:
        region = Region("Layer " + str(layerNumber), world.player, world.multiworld)

        # layerNumber - 1 cause I want the index layer
        # [:switches] because I want only the x first switches for that layer

        switches_locations = generate_switches_location_for_layer(layerNumber - 1)
        switches_locations_cropped = switches_locations[:switches]

        mappedLocations = map_locations(switches_locations_cropped)
        region.add_locations(mappedLocations)

        current_cave: DomeKeeperLocationData = caves_location.pop(0)

        cave_location: DomeKeeperLocation = DomeKeeperLocation(world.player, current_cave.name, current_cave.code, region)
        cave_location.progress_type = LocationProgressType.PRIORITY
        region.locations.append(cave_location)

        if layerNumber == 1:
            region.add_locations(map_locations(location_table_easy_upgrades))
        if layerNumber == 2:
            region.add_locations(map_locations(location_table_normal_upgrades))
        if layerNumber == 3:
            region.add_locations(map_locations(location_table_hard_upgrades))
        
        world.multiworld.regions.append(region)
        if layerNumber >= 2:
            world.multiworld.get_region('Layer ' + str(layerNumber - 1), world.player).connect(region)

        layerNumber += 1
    
    # link up our region with the entrance we just made
    world.multiworld.get_region('Menu', world.player).connect(world.multiworld.get_region('Layer 1', world.player))

    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(
        world.goalItems, world.player
    )

def map_locations(locations: list[DomeKeeperLocationData]) -> Dict[str, int]:
    return {location.name: location.code for location in locations}

class DomeKeeperLocation(Location):
    game: str = "Dome Keeper"