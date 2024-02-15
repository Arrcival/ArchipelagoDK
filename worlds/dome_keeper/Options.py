from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, DeathLink, Range, Toggle


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

class DrillUpgradesAmount(Range):
    """The amount of drill upgrades (when playing engineer) in the item pool.
    It is not recommended to go lower than 6~7 on large/huge maps.
    """
    range_start = 4
    range_end = 10
    default = 7
    display_name = "Drill upgrades"

class KineticSpheresUpgradesAmount(Range):
    """The amount of kinetic spheres upgrades (when playing assessor) in the item pool.
    It is not recommended to go lower than 6~7 on large/huge maps."""
    range_start = 4
    range_end = 10
    default = 7
    display_name = "Kinetic spheres upgrades"

class SphereLifetimeUpgradesAmount(Range):
    """The amount of sphere lifetime upgrades (when playing assessor) in the item pool."""
    range_start = 4
    range_end = 15
    default = 6
    display_name = "Sphere lifetime upgrades"

class ExtraCobaltFiller(Range):
    """The amount of extra cobalt added in the item pool as filler items."""
    range_start = 0
    range_end = 10
    default = 0
    display_name = "Extra cobalt items"

class ColoredLayersProgression(Toggle):
    """Locks color layers with an item for progression.
    """
    internal_name = "colored_layers"
    display_name = "Colored layers progression"

class MiningEverythingVictory(Toggle):
    """You can only claim victory if you mined every single tile of the map
    """
    display_name = "Mining everything goal"

@dataclass
class DomeKeeperOptions(PerGameCommonOptions):
    keeper: Keeper
    dome: Dome
    dome_gadget: DomeGadget
    map_size: MapSize
    difficulty: Difficulty
    death_link: DeathLink
    drill_upgrades: DrillUpgradesAmount
    kinetic_spheres: KineticSpheresUpgradesAmount
    colored_layers: ColoredLayersProgression
    sphere_lifetime: SphereLifetimeUpgradesAmount
    extra_cobalt: ExtraCobaltFiller
    mining_everything: MiningEverythingVictory