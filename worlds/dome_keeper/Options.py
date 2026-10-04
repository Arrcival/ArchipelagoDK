from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, DeathLink, Range, StartInventoryPool, Toggle

class HaveDLC(Toggle):
    """Do you own the DLC? Beastmaster and infiltrator are only available if you own the DLC. If unchecked, picking random will be only Engineer/Assessor."""
    internal_name = "have_dlc"
    display_name = "Have DLC"
    default = True

class Keeper(Choice):
    """What Keeper do you wish to play with."""
    internal_name = "keeper"
    display_name = "Keeper"
    option_Engineer = 0
    option_Assessor = 1
    option_Infiltrator = 2
    option_Beastmaster = 3
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

class SmallLayersAmount(Range):
    """How many layers there is in a small map"""
    internal_name = "small_layers"
    range_start = 3
    range_end = 6
    default = 4
    display_name = "Small map layers amount"

class MediumLayersAmount(Range):
    """How many layers there is in a medium map"""
    internal_name = "medium_layers"
    range_start = 3
    range_end = 8
    default = 6
    display_name = "Medium map layers amount"

class LargeLayersAmount(Range):
    """How many layers there is in a large map"""
    internal_name = "large_layers"
    range_start = 3
    range_end = 10
    default = 7
    display_name = "Large map layers amount"

class HugeLayersAmount(Range):
    """How many layers there is in a huge map"""
    internal_name = "huge_layers"
    range_start = 3
    range_end = 10
    default = 8
    display_name = "Huge map layers amount"

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
    display_name = "Engineer - Drill upgrades"

class KineticSpheresUpgradesAmount(Range):
    """The amount of kinetic spheres upgrades (when playing assessor) in the item pool.
    It is not recommended to go lower than 6~7 on large/huge maps."""
    internal_name = "kinetic_spheres"
    range_start = 5
    range_end = 10
    default = 7
    display_name = "Assessor - Kinetic spheres upgrades"

class SphereLifetimeUpgradesAmount(Range):
    """The amount of sphere lifetime upgrades (when playing assessor) in the item pool."""
    internal_name = "sphere_lifetime"
    range_start = 4
    range_end = 15
    default = 6
    display_name = "Assessor - Sphere lifetime upgrades"

class KunaiUpgradesAmount(Range):
    """The amount of kunai upgrades (when playing infiltrator) in the item pool.
    It is not recommended to go lower than 6~7 on large/huge maps.
    """
    internal_name = "kunai_upgrades"
    range_start = 5
    range_end = 10
    default = 7
    display_name = "Infiltrator - Kunai upgrades"

class BeastmasterMiningUpgradesAmount(Range):
    """The amount of beastmaster mining upgrades
    It is not recommended to go lower than 6~7 on large/huge maps.
    """
    internal_name = "beastmaster_mining_amount"
    range_start = 4
    range_end = 14
    default = 7
    display_name = "Beastmaster - Mining upgrade amount"

class CatgoblinsAmount(Range):
    """The amount of catgoblins (when playing beastmaster) in the item pool.
    It is not recommended to go lower than 6~7 on large/huge maps.
    """
    internal_name = "catgoblins_amount"
    range_start = 4
    range_end = 14
    default = 7
    display_name = "Beastmaster - Catgoblins amount"

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

class ExtraWaterFiller(Range):
    """The amount of extra water added in the item pool as filler items."""
    internal_name = "extra_water"
    range_start = 0
    range_end = 10
    default = 0
    display_name = "Extra water items"

class ExtraIronFiller(Range):
    """The amount of extra iron added in the item pool as filler items."""
    internal_name = "extra_iron"
    range_start = 0
    range_end = 15
    default = 3
    display_name = "Extra iron items"

class TrapWaveShortener(Range):
    """The amount of trap items that shorten your current wave cooldown."""
    internal_name = "trap_wave"
    range_start = 0
    range_end = 15
    default = 0
    display_name = "Trap wave shortener"

class ProgressionType(Choice):
    """The type of progression you want to play with."""
    internal_name = "progression_type"
    display_name = "Progression type"
    option_Relic_Hunt = 0
    option_Guild_Assignments = 1
    default = 0

class MiningEverythingVictory(Toggle):
    """You can only claim victory if you mined every single tile of the map"""
    internal_name = "mining_everything"
    display_name = "Mining everything goal"

class DefaultMiningStrength(Range):
    """
    Default percentage of mining strength in guild assignments.
    100 means 100% which is starting as normal
    """
    internal_name = "default_mining_strength"
    display_name = "Mining - Default strength"
    range_start = 80
    range_end = 120
    default = 100

class MiningStrengthBonusValue(Range):
    """Mining strength bonus gain in guild assignments for checks"""
    internal_name = "mining_strength_checks"
    display_name = "Mining - Bonus % strength per check"
    range_start = 0
    range_end = 10
    default = 5

class MiningStrengthBonusAmount(Range):
    """Mining strength bonus gain in guild assignments for checks"""
    internal_name = "mining_strength_amount"
    display_name = "Mining - Bonus strength check amount"
    range_start = 0
    range_end = 10
    default = 10

class DefaultMovementSpeed(Range):
    """
    Default percentage of movement speed in guild assignments
    100 means 100% which is starting as normal
    Infiltrator has no speed bonuses
    """
    internal_name = "default_movement_speed"
    display_name = "Movement - Default speed"
    range_start = 80
    range_end = 120
    default = 100

class MovementSpeedBonusValue(Range):
    """Movement speed bonus gain in guild assignments for checks
    Infiltrator has no speed bonuses"""
    internal_name = "movement_speed_checks"
    display_name = "Movement - Bonus % speed per check"
    range_start = 0
    range_end = 10
    default = 5

class MovementSpeedBonusAmount(Range):
    """Movement speed bonus amount in guild assignments for checks
    Infiltrator has no speed bonuses"""
    internal_name = "movement_speed_amount"
    display_name = "Movement - Bonus speed check amount"
    range_start = 0
    range_end = 10
    default = 5

class MustBeChallengeMode(Toggle):
    """Progression locations are flagged as progression in challenge mode instead of regular."""
    internal_name = "challenge_mode"
    display_name = "Challenge mode"

class AssignmentCompletionGoal(Range):
    """How many guild assignments you have to clear to clear the world."""
    internal_name = "assignment_amount"
    display_name = "Assignment completion amount"
    range_start = 1
    range_end = 25
    default = 16

class StartingWaterItems(Range):
    """How many iron rewards are replaced with starting water."""
    internal_name = "starting_water"
    range_start = 0
    range_end = 10
    default = 7
    display_name = "Water rewards"

class StartingCobaltItems(Range):
    """How many iron rewards are replaced with starting cobalt."""
    internal_name = "starting_cobalt"
    range_start = 0
    range_end = 10
    default = 5
    display_name = "Cobalt rewards"

class StartingAssignment(Choice):
    """The first assignment you want to start with."""
    internal_name = "first_assignment"
    display_name = "First assignment"
    option_Showdown = 0
    option_Iron_contribution = 1
    option_Upside_down = 2
    option_Maze = 3
    option_Projectile_hell = 4
    option_Dense_iron = 5
    option_Barren_lands = 6
    option_Defective_weapon = 7
    option_Heavy_hitters = 8
    option_Swiss_cheese = 9
    option_Logistical_problem = 10
    option_High_risk = 11
    option_Monster_masses = 12
    option_Iron_shortage = 13
    option_Mining_problem = 14
    option_Cobalt_contribution = 15
    option_Broken_comms = 16
    option_Darkness = 17
    option_Tree_Farm = 18
    option_Acid_Rain = 19
    option_Hazardous_Iron = 20
    option_Emergency = 21
    option_Brutal_Monsters = 22
    option_Logistical_Nightmare = 23
    option_Survival_of_the_Fittest = 24
    default = "random"

@dataclass
class DomeKeeperOptions(PerGameCommonOptions):
    have_dlc: HaveDLC
    keeper: Keeper
    dome: Dome
    dome_gadget: DomeGadget
    map_size: MapSize
    small_layers: SmallLayersAmount
    medium_layers: MediumLayersAmount
    large_layers: LargeLayersAmount
    huge_layers: HugeLayersAmount
    difficulty: Difficulty
    death_link: DeathLink
    drill_upgrades: DrillUpgradesAmount
    kinetic_spheres: KineticSpheresUpgradesAmount
    sphere_lifetime: SphereLifetimeUpgradesAmount
    kunai_upgrades: KunaiUpgradesAmount
    beastmaster_mining_amount: BeastmasterMiningUpgradesAmount
    catgoblins_amount: CatgoblinsAmount
    droneyard_drones: DroneyardDronesAmount
    extra_cobalt: ExtraCobaltFiller
    extra_water: ExtraWaterFiller
    extra_iron: ExtraIronFiller
    trap_wave: TrapWaveShortener
    mining_everything: MiningEverythingVictory
    progression_type: ProgressionType
    challenge_mode: MustBeChallengeMode
    starting_water: StartingWaterItems
    starting_cobalt: StartingCobaltItems
    default_mining_strength: DefaultMiningStrength
    mining_strength_value: MiningStrengthBonusValue
    mining_strength_amount: MiningStrengthBonusAmount
    default_movement_speed: DefaultMovementSpeed
    movement_speed_value: MovementSpeedBonusValue
    movement_speed_amount: MovementSpeedBonusAmount
    first_assignment: StartingAssignment
    assignment_amount: AssignmentCompletionGoal
    start_inventory_from_pool: StartInventoryPool