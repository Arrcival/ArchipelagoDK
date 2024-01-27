import typing

from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, DeathLink


class Keeper(Choice):
    """What Keeper do you wish to play with."""
    display_name = "Keeper"
    option_Engineer = 0
    option_Assessor = 1
    default = "random"

class Dome(Choice):
    """What Dome do you wish to play with."""
    display_name = "Dome"
    option_Laser = 0
    option_Sword = 1
    option_Artillery = 2
    option_Tesla = 3
    default = "random"

class DomeGadget(Choice):
    """What Dome gadget do you wish to play with."""
    display_name = "Dome gadget"
    option_Shield = 0
    option_Orchard = 1
    option_Repellent = 2
    default = "random"

class MapSize(Choice):
    """What map size do you wish to play with."""
    display_name = "Map size"
    option_Small = 0
    option_Medium = 1
    option_Large = 2
    option_Huge = 3
    default = 3

class Difficulty(Choice):
    """What difficulty do you wish to play with."""
    display_name = "Difficulty"
    option_Normal = 0
    option_Hard = 1
    option_Brutal = 2
    option_YouAskedForIt = 3
    default = 2

@dataclass
class DomeKeeperOptions(PerGameCommonOptions):
    keeper: Keeper
    dome: Dome
    dome_gadget: DomeGadget
    map_size: MapSize
    difficulty: Difficulty
    death_link: DeathLink