from BaseClasses import ItemClassification as IC
from typing import NamedTuple, Dict

dome_keeper_index = 4242000

class ItemData(NamedTuple):
    name: str
    tech_name: str
    count: int = 1
    classification: IC = IC.useful

class ItemDataCode():
    code: int
    data: ItemData

    def __init__(self, code: int, data: ItemData):
        self.code = code
        self.data = data

item_engineer: ItemDataCode = ItemDataCode(dome_keeper_index + 10, ItemData("Keeper upgrade", "keeperUpgrade", 6))
item_assessor: ItemDataCode = ItemDataCode(dome_keeper_index + 10, ItemData("Keeper upgrade", "keeperUpgrade", 10))
item_laser: ItemDataCode = ItemDataCode(dome_keeper_index + 30, ItemData("Dome upgrade", "domeUpgrade", 6))
item_sword: ItemDataCode = ItemDataCode(dome_keeper_index + 30, ItemData("Dome upgrade", "domeUpgrade", 10))
item_artillery: ItemDataCode = ItemDataCode(dome_keeper_index + 30, ItemData("Dome upgrade", "domeUpgrade", 9))
item_tesla: ItemDataCode = ItemDataCode(dome_keeper_index + 30, ItemData("Dome upgrade", "domeUpgrade", 12))
item_gadget: ItemDataCode = ItemDataCode(dome_keeper_index + 50, ItemData("Primary gadget upgrade", "gadgetUpgrade", 12))
item_cobalt: ItemDataCode = ItemDataCode(dome_keeper_index + 4, ItemData("Extra cobalt", "cobaltGeneration", classification=IC.filler))

item_table: Dict[int, ItemData] = {
    dome_keeper_index + 10: item_engineer.data,
    dome_keeper_index + 30: item_laser.data,
    dome_keeper_index + 50: item_gadget.data,
    dome_keeper_index + 4: item_cobalt.data,
}