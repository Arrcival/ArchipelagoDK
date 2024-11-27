
from typing import Any, Dict
from .Options import ColoredLayersProgression, MapSize, DrillUpgradesAmount, KineticSpheresUpgradesAmount, ExtraCobaltFiller, Keeper, Dome, DomeGadget

no_progression_short_settings = {
    ColoredLayersProgression.internal_name: ColoredLayersProgression.option_false,
    MapSize.internal_name: MapSize.option_Medium,
    DrillUpgradesAmount.internal_name: 5,
    KineticSpheresUpgradesAmount.internal_name: 5,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

no_progression_settings = {
    ColoredLayersProgression.internal_name: ColoredLayersProgression.option_false,
    MapSize.internal_name: MapSize.option_Huge,
    DrillUpgradesAmount.internal_name: 7,
    KineticSpheresUpgradesAmount.internal_name: 7,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

progression_short_settings = {
    ColoredLayersProgression.internal_name: ColoredLayersProgression.option_true,
    MapSize.internal_name: MapSize.option_Medium,
    DrillUpgradesAmount.internal_name: 5,
    KineticSpheresUpgradesAmount.internal_name: 5,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

progression_average_settings = {
    ColoredLayersProgression.internal_name: ColoredLayersProgression.option_true,
    MapSize.internal_name: MapSize.option_Huge,
    DrillUpgradesAmount.internal_name: 7,
    KineticSpheresUpgradesAmount.internal_name: 7,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

progression_hard_settings = {
    ColoredLayersProgression.internal_name: ColoredLayersProgression.option_true,
    MapSize.internal_name: MapSize.option_Huge,
    DrillUpgradesAmount.internal_name: 7,
    KineticSpheresUpgradesAmount.internal_name: 7,
    ExtraCobaltFiller.internal_name: 0,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random"
}

progression_hard_dl_settings = {
    ColoredLayersProgression.internal_name: ColoredLayersProgression.option_true,
    MapSize.internal_name: MapSize.option_Huge,
    DrillUpgradesAmount.internal_name: 7,
    KineticSpheresUpgradesAmount.internal_name: 7,
    ExtraCobaltFiller.internal_name: 0,
    Keeper.internal_name: "random",
    Dome.internal_name: "random",
    DomeGadget.internal_name: "random",
    "death_link": "true"
}

dk_options_presets: Dict[str, Dict[str, Any]] = {
    "No progression - Short": no_progression_short_settings,
    "No progression": no_progression_settings,
    "Progression - Short": progression_short_settings,
    "Progression - Average": progression_average_settings,
    "Progression - Hard": progression_hard_settings,
    "Progression - Hard (w/ DL)": progression_hard_dl_settings,
}