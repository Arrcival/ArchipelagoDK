from typing import NamedTuple, Optional, List
from BaseClasses import Entrance, MultiWorld, Region
from .Locations import DomeKeeperLocation, location_table

class DomeKeeperRegionData(NamedTuple):
    locations: Optional[List[str]]
    region_exits: Optional[List[str]]

def create_regions(world, player: int):

    world.regions += [
        create_region(world, player, 'Menu', exits=['Menu exit']),
        create_region(world, player, 'On Map', locations=location_table)
    ]

    # link up our region with the entrance we just made
    world.get_entrance('Menu exit', player).connect(world.get_region('On Map', player))

def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, world)
    if locations:
        for name, loc in locations.items():
            ret.locations.append(DomeKeeperLocation(player, name, loc.code, ret))
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret