from typing import Dict, NamedTuple, Optional


class DomeKeeperLocationData(NamedTuple):
    name: str
    code: Optional[int] = None

UPGRADES_AMOUNT = 12

SWITCHES_FIRST_ID = 4243101
SWITCHES_MAX_AMOUNT = 61

CAVE_FIRST_ID = 4243020
CAVES_MAX_AMOUNT = 7

location_table_easy_upgrades : Dict[str, DomeKeeperLocationData] = {
    "Upgrade Iron 1":  DomeKeeperLocationData("Upgrade unlock",     4243001),
    "Upgrade Iron 2":  DomeKeeperLocationData("Upgrade unlock",     4243002),
    "Upgrade Water 1":  DomeKeeperLocationData("Upgrade unlock",    4243005),
    "Upgrade Water 2":  DomeKeeperLocationData("Upgrade unlock",    4243006),
    "Upgrade Iron and Water 1":  DomeKeeperLocationData("Upgrade unlock",   4243009),
    "Upgrade Iron and Water 2":  DomeKeeperLocationData("Upgrade unlock",   4243010),
}

location_table_normal_upgrades : Dict[str, DomeKeeperLocationData] = {
    "Upgrade Iron 3":  DomeKeeperLocationData("Upgrade unlock",     4243003),
    "Upgrade Water 3":  DomeKeeperLocationData("Upgrade unlock",    4243007),
    "Upgrade Iron and Water 3":  DomeKeeperLocationData("Upgrade unlock",   4243011),
}

location_table_hard_upgrades : Dict[str, DomeKeeperLocationData] = {
    "Upgrade Iron 4":  DomeKeeperLocationData("Upgrade unlock",     4243004),
    "Upgrade Water 4":  DomeKeeperLocationData("Upgrade unlock",    4243008),
    "Upgrade Iron and Water 4":  DomeKeeperLocationData("Upgrade unlock",   4243012),
}

location_table_upgrades: Dict[str, DomeKeeperLocationData] = location_table_easy_upgrades | location_table_normal_upgrades | location_table_hard_upgrades

def generate_locations_data() -> Dict[str, DomeKeeperLocationData] :
    rtr: Dict[str, DomeKeeperLocationData] = location_table_upgrades.copy()
    rtr = rtr | generate_switches_location()
    rtr = rtr | generate_caves_location()
    return rtr

def generate_switches_location() -> Dict[str, DomeKeeperLocationData] :
    rtr = {}
    for i in range(SWITCHES_MAX_AMOUNT):
        rtr["Switch " + str(i + 1)] = DomeKeeperLocationData("Switch " + str(i + 1), SWITCHES_FIRST_ID + i)
    return rtr

def generate_caves_location() -> Dict[str, DomeKeeperLocationData] :
    rtr = {}
    for i in range(CAVES_MAX_AMOUNT):
        rtr["Cave " + str(i + 1)] = DomeKeeperLocationData("Cave " + str(i + 1), CAVE_FIRST_ID + i)
    return rtr