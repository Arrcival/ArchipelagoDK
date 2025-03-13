from typing import List

from Options import DeathLink, ProgressionBalancing, Accessibility, OptionGroup
from .Options import (AssignmentCompletionGoal, Dome, ExtraIronFiller, ExtraWaterFiller, Keeper, DomeGadget, MapSize, Difficulty, DrillUpgradesAmount, ProgressionType,
                      KineticSpheresUpgradesAmount, SphereLifetimeUpgradesAmount, DroneyardDronesAmount, ExtraCobaltFiller, MiningEverythingVictory,
                      MustBeChallengeMode, StartingWaterItems, StartingCobaltItems, StartingAssignment, TrapWaveShortener)

dk_option_groups: List[OptionGroup] = [
    OptionGroup("General", [
        ProgressionType,
        DeathLink,
        ProgressionBalancing,
        Accessibility,
        TrapWaveShortener
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
        ExtraCobaltFiller,
        ExtraWaterFiller,
        ExtraIronFiller
    ]),
    OptionGroup("Guild assignments", [
        MustBeChallengeMode,
        StartingWaterItems,
        StartingCobaltItems,
        StartingAssignment,
        AssignmentCompletionGoal
    ]),
]