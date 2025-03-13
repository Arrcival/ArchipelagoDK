
from typing import Any, Dict
from .Options import MustBeChallengeMode, ProgressionType, MapSize, DrillUpgradesAmount, KineticSpheresUpgradesAmount, ExtraCobaltFiller, Keeper, Dome, DomeGadget, StartingAssignment, StartingCobaltItems, StartingWaterItems, TrapWaveShortener

no_progression_short_settings = {
    ProgressionType.internal_name: ProgressionType.option_Relic_Hunt_No_Progression,
    MapSize.internal_name: MapSize.option_Medium,
    DrillUpgradesAmount.internal_name: 5,
    KineticSpheresUpgradesAmount.internal_name: 5,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

no_progression_long_settings = {
    ProgressionType.internal_name: ProgressionType.option_Relic_Hunt_No_Progression,
    MapSize.internal_name: MapSize.option_Huge,
    DrillUpgradesAmount.internal_name: 7,
    KineticSpheresUpgradesAmount.internal_name: 7,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

progression_short_settings = {
    ProgressionType.internal_name: ProgressionType.option_Relic_Hunt_Progression_Layers,
    MapSize.internal_name: MapSize.option_Medium,
    DrillUpgradesAmount.internal_name: 5,
    KineticSpheresUpgradesAmount.internal_name: 5,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

progression_long_settings = {
    ProgressionType.internal_name: ProgressionType.option_Relic_Hunt_Progression_Layers,
    MapSize.internal_name: MapSize.option_Huge,
    DrillUpgradesAmount.internal_name: 7,
    KineticSpheresUpgradesAmount.internal_name: 7,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

progression_long_dl_settings = {
    ProgressionType.internal_name: ProgressionType.option_Relic_Hunt_Progression_Layers,
    MapSize.internal_name: MapSize.option_Huge,
    DrillUpgradesAmount.internal_name: 7,
    KineticSpheresUpgradesAmount.internal_name: 7,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random",
    "death_link": "true"
}

progression_ga_settings = {
    ProgressionType.internal_name: ProgressionType.option_Guild_Assignments,
    StartingWaterItems.internal_name: 5,
    StartingCobaltItems.internal_name: 3,
    StartingAssignment.internal_name: "random",
    MustBeChallengeMode.internal_name: MustBeChallengeMode.option_false,
    TrapWaveShortener.internal_name: 0,
}

progression_ga_challenge_settings = {
    ProgressionType.internal_name: ProgressionType.option_Guild_Assignments,
    StartingWaterItems.internal_name: 5,
    StartingCobaltItems.internal_name: 3,
    StartingAssignment.internal_name: "random",
    MustBeChallengeMode.internal_name: MustBeChallengeMode.option_true,
    TrapWaveShortener.internal_name: 0,
}

progression_ga_challenge_hard_settings = {
    ProgressionType.internal_name: ProgressionType.option_Guild_Assignments,
    StartingWaterItems.internal_name: 4,
    StartingCobaltItems.internal_name: 2,
    StartingAssignment.internal_name: "random",
    MustBeChallengeMode.internal_name: MustBeChallengeMode.option_true,
    TrapWaveShortener.internal_name: 5,
}

dk_options_presets: Dict[str, Dict[str, Any]] = {
    "Relic hunt - Short": no_progression_short_settings,
    "Relic hunt - Long": no_progression_long_settings,
    "Relic hunt with progression - Short": progression_short_settings,
    "Relic hunt with progression - Long": progression_long_settings,
    "Relic hunt with progression - Long (w/ DL)": progression_long_dl_settings,
    "Guild assignment - Regular": progression_ga_settings,
    "Guild assignment - Challenge": progression_ga_challenge_settings,
    "Guild assignment - Challenge hard": progression_ga_challenge_hard_settings,
}