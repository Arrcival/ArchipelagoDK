from typing import Dict, NamedTuple, Optional
from BaseClasses import Location

class DomeKeeperLocation(Location):
    game: str = "Dome Keeper"

class DomeKeeperLocationData(NamedTuple):
    name: str
    code: Optional[int] = None

location_table: Dict[str, DomeKeeperLocationData] = {
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
    "Switch found 1":  DomeKeeperLocationData("Switch found unlock",  4243101),
    "Switch found 2":  DomeKeeperLocationData("Switch found unlock",  4243102),
    "Switch found 3":  DomeKeeperLocationData("Switch found unlock",  4243103),
    "Switch found 4":  DomeKeeperLocationData("Switch found unlock",  4243104),
    "Switch found 5":  DomeKeeperLocationData("Switch found unlock",  4243105),
    "Switch found 6":  DomeKeeperLocationData("Switch found unlock",  4243106),
    "Switch found 7":  DomeKeeperLocationData("Switch found unlock",  4243107),
    "Switch found 8":  DomeKeeperLocationData("Switch found unlock",  4243108),
    "Switch found 9":  DomeKeeperLocationData("Switch found unlock",  4243109),
    "Switch found 10":  DomeKeeperLocationData("Switch found unlock", 4243110),
    "Switch found 11":  DomeKeeperLocationData("Switch found unlock", 4243111),
    "Switch found 12":  DomeKeeperLocationData("Switch found unlock", 4243112),
    "Switch found 13":  DomeKeeperLocationData("Switch found unlock", 4243113),
    "Switch found 14":  DomeKeeperLocationData("Switch found unlock", 4243114),
    "Switch found 15":  DomeKeeperLocationData("Switch found unlock", 4243115),
    "Switch found 16":  DomeKeeperLocationData("Switch found unlock", 4243116),
    "Switch found 17":  DomeKeeperLocationData("Switch found unlock", 4243117),
    "Switch found 18":  DomeKeeperLocationData("Switch found unlock", 4243118),
    "Switch found 19":  DomeKeeperLocationData("Switch found unlock", 4243119),
    "Switch found 20":  DomeKeeperLocationData("Switch found unlock", 4243120),
    "Switch found 21":  DomeKeeperLocationData("Switch found unlock", 4243121),
    "Switch found 22":  DomeKeeperLocationData("Switch found unlock", 4243122),
}