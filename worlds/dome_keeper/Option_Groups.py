from typing import List

from Options import DeathLink, ProgressionBalancing, Accessibility, OptionGroup
from .Options import (Dome, Keeper, DomeGadget, MapSize, Difficulty, DrillUpgradesAmount, ProgressionType,
                      KineticSpheresUpgradesAmount, SphereLifetimeUpgradesAmount, DroneyardDronesAmount, ExtraCobaltFiller, MiningEverythingVictory,
                      MustBeChallengeMode, StartingWaterItems, StartingCobaltItems, StartingAssignment)

dk_option_groups: List[OptionGroup] = [
    OptionGroup("General", [
        ProgressionType,
        DeathLink,
        ProgressionBalancing,
        Accessibility,
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
    ]),
    OptionGroup("Guild assignments", [
        MustBeChallengeMode,
        StartingWaterItems,
        StartingCobaltItems,
        StartingAssignment,
    ]),
]