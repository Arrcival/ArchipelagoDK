from typing import NamedTuple, Optional, List, Dict, TYPE_CHECKING
from BaseClasses import Location, LocationProgressType, Region
from .Locations import (
    DomeKeeperLocationData,
    generate_caves_location, 
    generate_switches_location, 
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

    switch_locations = generate_switches_location()
    caves_location: list[DomeKeeperLocationData] = list(generate_caves_location().values())
    switchesPerLayer = world.switchesPerLayer

    layerNumber = 1
    switchIndex = 0
    for switches in switchesPerLayer:
        region = Region("Layer " + str(layerNumber), world.player, world.multiworld)
        mappedLocations = map_locations_switches(switch_locations, switchIndex, switches)
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

        switchIndex += switches
        layerNumber += 1
    
    # link up our region with the entrance we just made
    world.multiworld.get_region('Menu', world.player).connect(world.multiworld.get_region('Layer 1', world.player))

    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(
        world.goalItems, world.player
    )


def map_locations_switches(locations: Dict[str, DomeKeeperLocationData], switchIndex, switches) -> Dict[str, int]:
    rtr: Dict[str, int] = {}
    for i in range(switchIndex, switchIndex + switches):
        switchName = "Switch " + str(i + 1)
        rtr[switchName] = locations[switchName].code
    return rtr

def map_locations(locations: Dict[str, DomeKeeperLocationData]) -> Dict[str, int]:
    rtr: Dict[str, int] = {}
    for key in locations.keys():
        rtr[key] = locations[key].code
    return rtr

class DomeKeeperLocation(Location):
    game: str = "Dome Keeper"