from typing import Dict, NamedTuple, Optional
from BaseClasses import Location
from worlds.dome_keeper.Items import MAX_UPGRADES_POSSIBLE

class DomeKeeperLocation(Location):
    game: str = "Dome Keeper"

class DomeKeeperLocationData(NamedTuple):
    name: str
    code: Optional[int] = None

UPGRADES_AMOUNT = 12

SWITCHES_AMOUNT = MAX_UPGRADES_POSSIBLE - UPGRADES_AMOUNT
SWITCHES_FIRST_ID = 4243101

location_table_upgrades: Dict[str, DomeKeeperLocationData] = {
    "Upgrade Iron 1":  DomeKeeperLocationData("Upgrade unlock",     4243001),
    "Upgrade Iron 2":  DomeKeeperLocationData("Upgrade unlock",     4243002),
    "Upgrade Iron 3":  DomeKeeperLocationData("Upgrade unlock",     4243003),
    "Upgrade Iron 4":  DomeKeeperLocationData("Upgrade unlock",     4243004),
    "Upgrade Water 1":  DomeKeeperLocationData("Upgrade unlock",    4243005),
    "Upgrade Water 2":  DomeKeeperLocationData("Upgrade unlock",    4243006),
    "Upgrade Water 3":  DomeKeeperLocationData("Upgrade unlock",    4243007),
    "Upgrade Water 4":  DomeKeeperLocationData("Upgrade unlock",    4243008),
    "Upgrade Iron and Water 1":  DomeKeeperLocationData("Upgrade unlock",   4243009),
    "Upgrade Iron and Water 2":  DomeKeeperLocationData("Upgrade unlock",   4243010),
    "Upgrade Iron and Water 3":  DomeKeeperLocationData("Upgrade unlock",   4243011),
    "Upgrade Iron and Water 4":  DomeKeeperLocationData("Upgrade unlock",   4243012),
}

def generate_locations() -> Dict[str, DomeKeeperLocationData] :
    rtr = location_table_upgrades.copy()
    for i in range(SWITCHES_AMOUNT):
        rtr["Switch found " + str(i + 1)] = DomeKeeperLocationData("Switch found", SWITCHES_FIRST_ID + i)
    return rtr

def get_locations_amount() -> int:
    return len(location_table_upgrades.keys()) + SWITCHES_AMOUNT