from Options import DeathLink, ProgressionBalancing, Accessibility, OptionGroup
from .Options import (
    AssignmentCompletionGoal, Dome, ExtraIronFiller, ExtraWaterFiller, Keeper, DomeGadget, MapSize, Difficulty, 
    DrillUpgradesAmount, ProgressionType, KineticSpheresUpgradesAmount, SphereLifetimeUpgradesAmount, BeastmasterMiningUpgradesAmount, DroneyardDronesAmount, 
    ExtraCobaltFiller, MiningEverythingVictory, MustBeChallengeMode, StartingWaterItems, StartingCobaltItems, 
    StartingAssignment, TrapWaveShortener, KunaiUpgradesAmount, CatgoblinsAmount, HaveDLC,
    DefaultMiningStrength, DefaultMovementSpeed, MiningStrengthBonusValue, MiningStrengthBonusAmount, MovementSpeedBonusValue, MovementSpeedBonusAmount
    )

dk_option_groups: list[OptionGroup] = [
    OptionGroup("General", [
        ProgressionType,
        DeathLink,
        ProgressionBalancing,
        Accessibility,
        TrapWaveShortener,
        HaveDLC
    ]),
    OptionGroup("Relic hunt - General", [
        Dome,
        Keeper,
        DomeGadget,
        MapSize,
        Difficulty,
        MiningEverythingVictory,
    ]),
    OptionGroup("Relic hunt - Items amount", [
        DrillUpgradesAmount,
        KineticSpheresUpgradesAmount,
        SphereLifetimeUpgradesAmount,
        DroneyardDronesAmount,
        KunaiUpgradesAmount,
        BeastmasterMiningUpgradesAmount,
        CatgoblinsAmount,
        ExtraCobaltFiller,
        ExtraWaterFiller,
        ExtraIronFiller
    ]),
    OptionGroup("Guild assignments", [
        MustBeChallengeMode,
        StartingWaterItems,
        StartingCobaltItems,
        StartingAssignment,
        AssignmentCompletionGoal,
        DefaultMiningStrength,
        MiningStrengthBonusValue,
        MiningStrengthBonusAmount,
        DefaultMovementSpeed,
        MovementSpeedBonusValue,
        MovementSpeedBonusAmount
    ]),
]