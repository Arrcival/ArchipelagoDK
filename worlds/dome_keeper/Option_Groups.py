from typing import List

from Options import DeathLink, ProgressionBalancing, Accessibility, OptionGroup
from .Options import (Dome, Keeper, DomeGadget, MapSize, Difficulty, DrillUpgradesAmount, ColoredLayersProgression,
                      KineticSpheresUpgradesAmount, SphereLifetimeUpgradesAmount, DroneyardDronesAmount, ExtraCobaltFiller, MiningEverythingVictory)

dk_option_groups: List[OptionGroup] = [
    OptionGroup("General", [
        Dome,
        Keeper,
        DomeGadget,
        MapSize,
        Difficulty,
        ColoredLayersProgression
    ]),
    OptionGroup("Item amount", [
        DrillUpgradesAmount,
        KineticSpheresUpgradesAmount,
        SphereLifetimeUpgradesAmount,
        DroneyardDronesAmount,
        ExtraCobaltFiller,
    ]),
    OptionGroup("Bonus", [
        MiningEverythingVictory,
    ]),
    OptionGroup("Advanced Options", [
        DeathLink,
        ProgressionBalancing,
        Accessibility,
    ]),
]