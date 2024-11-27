from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, DeathLink, Range, Toggle


class Keeper(Choice):
    """What Keeper do you wish to play with."""
    internal_name = "keeper"
    display_name = "Keeper"
    option_Engineer = 0
    option_Assessor = 1
    default = "random"

class Dome(Choice):
    """What Dome do you wish to play with."""
    internal_name = "dome"
    display_name = "Dome"
    option_Laser = 0
    option_Sword = 1
    option_Artillery = 2
    option_Tesla = 3
    default = "random"

class DomeGadget(Choice):
    """What Dome gadget do you wish to play with."""
    internal_name = "dome_gadget"
    display_name = "Dome gadget"
    option_Shield = 0
    option_Repellent = 1
    option_Orchard = 2
    option_Droneyard = 3
    default = "random"

class MapSize(Choice):
    """What map size do you wish to play with."""
    internal_name = "map_size"
    display_name = "Map size"
    option_Small = 0
    option_Medium = 1
    option_Large = 2
    option_Huge = 3
    default = 3

class Difficulty(Choice):
    """What difficulty do you wish to play with."""
    internal_name = "difficulty"
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
    internal_name = "drill_upgrades"
    range_start = 5
    range_end = 10
    default = 7
    display_name = "Drill upgrades"

class KineticSpheresUpgradesAmount(Range):
    """The amount of kinetic spheres upgrades (when playing assessor) in the item pool.
    It is not recommended to go lower than 6~7 on large/huge maps."""
    internal_name = "kinetic_spheres"
    range_start = 5
    range_end = 10
    default = 7
    display_name = "Kinetic spheres upgrades"

class SphereLifetimeUpgradesAmount(Range):
    """The amount of sphere lifetime upgrades (when playing assessor) in the item pool."""
    internal_name = "sphere_lifetime"
    range_start = 4
    range_end = 15
    default = 6
    display_name = "Sphere lifetime upgrades"

class DroneyardDronesAmount(Range):
    """The amount of droneyard drone upgrades (when using the droneyard) in the item pool."""
    internal_name = "droneyard_drones"
    range_start = 0
    range_end = 10
    default = 5
    display_name = "Droneyard drone upgrades"

class ExtraCobaltFiller(Range):
    """The amount of extra cobalt added in the item pool as filler items."""
    internal_name = "extra_cobalt"
    range_start = 0
    range_end = 10
    default = 0
    display_name = "Extra cobalt items"

class ColoredLayersProgression(Toggle):
    """Locks color layers with an item for progression."""
    internal_name = "colored_layers"
    display_name = "Colored layers progression"
    default = True

class MiningEverythingVictory(Toggle):
    """You can only claim victory if you mined every single tile of the map"""
    internal_name = "mining_everything"
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
    droneyard_drones: DroneyardDronesAmount
    extra_cobalt: ExtraCobaltFiller
    mining_everything: MiningEverythingVictory