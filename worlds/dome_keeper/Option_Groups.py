from Options import DeathLink, ProgressionBalancing, Accessibility, OptionGroup
from .Options import (
    AssignmentCompletionGoal, Dome, ExtraIronFiller, ExtraWaterFiller, HugeLayersAmount, Keeper, DomeGadget, LargeLayersAmount, MapSize, Difficulty, RelicExplosionDeathLink,
    DrillUpgradesAmount, MediumLayersAmount, ProgressionType, KineticSpheresUpgradesAmount, SmallLayersAmount, SphereLifetimeUpgradesAmount, BeastmasterMiningUpgradesAmount, DroneyardDronesAmount, 
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
        HaveDLC,
        RelicExplosionDeathLink
    ]),
    OptionGroup("Relic hunt - General", [
        Dome,
        Keeper,
        DomeGadget,
        Difficulty,
        MiningEverythingVictory,
    ]),
    OptionGroup("Relic hunt - Map", [
        MapSize,
        SmallLayersAmount,
        MediumLayersAmount,
        LargeLayersAmount,
        HugeLayersAmount
    ]),
    OptionGroup("Relic hunt - Items amount", [
        DrillUpgradesAmount,
        KineticSpheresUpgradesAmount,
        SphereLifetimeUpgradesAmount,
        KunaiUpgradesAmount,
        BeastmasterMiningUpgradesAmount,
        CatgoblinsAmount,
        DroneyardDronesAmount,
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