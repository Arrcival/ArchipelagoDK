from typing import Dict, NamedTuple, Optional

class DomeKeeperLocationData(NamedTuple):
    name: str
    code: Optional[int] = None

# Keeper, dome, gadget, progression layers, extra cobalt
MAX_ITEMS_POSSIBLE = 43 + 20 + 14 + 6 + 10

CAVE_FIRST_ID = 4243020
LAYERS_MAX_AMOUNT = 7

UPGRADES_LOCATIONS_AMOUNT = 12

SWITCHES_FIRST_ID = 4243101

LAYER_OFFSET = 30

location_table_easy_upgrades : list[DomeKeeperLocationData] = [
    DomeKeeperLocationData("Upgrade Iron 1",             4243001),
    DomeKeeperLocationData("Upgrade Iron 2",             4243002),
    DomeKeeperLocationData("Upgrade Water 1",            4243005),
    DomeKeeperLocationData("Upgrade Water 2",            4243006),
    DomeKeeperLocationData("Upgrade Iron and Water 1",   4243009),
    DomeKeeperLocationData("Upgrade Iron and Water 2",   4243010),
]

location_table_normal_upgrades : list[DomeKeeperLocationData] = [
    DomeKeeperLocationData("Upgrade Iron 3",             4243003),
    DomeKeeperLocationData("Upgrade Water 3",            4243007),
    DomeKeeperLocationData("Upgrade Iron and Water 3",   4243011),
]

location_table_hard_upgrades : list[DomeKeeperLocationData] = [
    DomeKeeperLocationData("Upgrade Iron 4",             4243004),
    DomeKeeperLocationData("Upgrade Water 4",            4243008),
    DomeKeeperLocationData("Upgrade Iron and Water 4",   4243012),
]

def generate_locations_data() -> list[DomeKeeperLocationData] :
    rtr: list[DomeKeeperLocationData] = []
    rtr.extend(location_table_easy_upgrades.copy())
    rtr.extend(location_table_normal_upgrades.copy())
    rtr.extend(location_table_hard_upgrades.copy())
    rtr.extend(generate_switches_locations())
    rtr.extend(generate_caves_locations())
    return rtr

def generate_switches_locations() -> list[DomeKeeperLocationData]:
    rtr = []
    for i in range(LAYERS_MAX_AMOUNT):
        layer_switches: list[DomeKeeperLocationData] = generate_switches_location_for_layer(i)
        rtr.extend(layer_switches)
    return rtr


def generate_switches_location_for_layer(layer: int) -> list[DomeKeeperLocationData]:
    rtr = []
    for i in range(LAYER_OFFSET):
        rtr.append(DomeKeeperLocationData("Layer " + str(layer + 1) + " - Switch " + str(i + 1), SWITCHES_FIRST_ID + (LAYER_OFFSET * layer) + i))
    return rtr

def generate_caves_locations() -> list[DomeKeeperLocationData] :
    rtr = []
    for i in range(LAYERS_MAX_AMOUNT):
        rtr.append(DomeKeeperLocationData("Layer " + str(i + 1) + " - Cave", CAVE_FIRST_ID + i))
    return rtr