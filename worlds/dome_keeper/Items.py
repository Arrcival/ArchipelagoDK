from BaseClasses import ItemClassification as IC
from typing import NamedTuple, Dict

dome_keeper_index = 4242000

MAX_UPGRADES_POSSIBLE = 31 + 20 + 14

class ItemData(NamedTuple):
    name: str
    count: int = 1
    classification: IC = IC.useful

class ItemDataCode():
    code: int
    data: ItemData

    def __init__(self, code: int, data: ItemData):
        self.code = code
        self.data = data

dome_keeper_index_engineer = dome_keeper_index
dome_keeper_index_assessor = dome_keeper_index + 10
dome_keeper_index_laser = dome_keeper_index + 20
dome_keeper_index_sword = dome_keeper_index + 30
dome_keeper_index_artillery = dome_keeper_index + 40
dome_keeper_index_tesla = dome_keeper_index + 50
dome_keeper_index_repellent = dome_keeper_index + 60
dome_keeper_index_shield = dome_keeper_index + 70
dome_keeper_index_orchard = dome_keeper_index + 80
dome_keeper_index_cobalt = dome_keeper_index + 90
dome_keeper_index_trap = dome_keeper_index + 91
dome_keeper_index_layers = dome_keeper_index + 100

item_filler_cobalt: ItemDataCode = ItemDataCode(dome_keeper_index_cobalt, ItemData("Extra cobalt", classification=IC.filler))
item_trap_wavestart: ItemDataCode = ItemDataCode(dome_keeper_index_trap, ItemData("Wave start", classification=IC.trap))


item_engineer_drill  : ItemDataCode = ItemDataCode(dome_keeper_index_engineer + 0, ItemData("Drill upgrade", classification=IC.progression))
item_engineer_jetpack: ItemDataCode = ItemDataCode(dome_keeper_index_engineer + 1, ItemData("Jetpack upgrade", 4))
item_engineer_carry  : ItemDataCode = ItemDataCode(dome_keeper_index_engineer + 2, ItemData("Carry upgrade", 4))

items_engineer = [item_engineer_jetpack, item_engineer_carry]

item_assessor_movement          : ItemDataCode = ItemDataCode(dome_keeper_index_assessor + 0, ItemData("Gravitational movement", 4))
item_assessor_spheres_strength  : ItemDataCode = ItemDataCode(dome_keeper_index_assessor + 1, ItemData("Kinetic spheres", classification=IC.progression))
item_assessor_bundles           : ItemDataCode = ItemDataCode(dome_keeper_index_assessor + 2, ItemData("Bundles upgrade", 4))
item_assessor_spheres_supply    : ItemDataCode = ItemDataCode(dome_keeper_index_assessor + 3, ItemData("Sphere supply upgrade", 6))
item_assessor_spheres_lifetime  : ItemDataCode = ItemDataCode(dome_keeper_index_assessor + 4, ItemData("Sphere lifetime upgrade"))
# one of the three upgrade and it's better upgrade
item_assessor_spheres_special   : ItemDataCode = ItemDataCode(dome_keeper_index_assessor + 5, ItemData("Sphere special upgrade", 2))
item_assessor_compression_mining: ItemDataCode = ItemDataCode(dome_keeper_index_assessor + 6, ItemData("Compression mining upgrade", 2))

items_assessor = [
    item_assessor_movement,
    item_assessor_bundles,
    item_assessor_spheres_supply,
    item_assessor_spheres_special,
    item_assessor_compression_mining,
]

item_laser_strength: ItemDataCode = ItemDataCode(dome_keeper_index_laser + 0, ItemData("Laser strength", 5))
item_laser_speed   : ItemDataCode = ItemDataCode(dome_keeper_index_laser + 1, ItemData("Laser speed", 3))
item_laser_sight   : ItemDataCode = ItemDataCode(dome_keeper_index_laser + 2, ItemData("Laser sight", 1))

items_laser = [item_laser_strength, item_laser_speed, item_laser_sight]

item_sword_strength  : ItemDataCode = ItemDataCode(dome_keeper_index_sword + 0, ItemData("Sword strength", 4))
item_sword_aimline   : ItemDataCode = ItemDataCode(dome_keeper_index_sword + 1, ItemData("Sword aim line", 1))
item_sword_stab      : ItemDataCode = ItemDataCode(dome_keeper_index_sword + 2, ItemData("Sword better stab", 4))
item_sword_reflection: ItemDataCode = ItemDataCode(dome_keeper_index_sword + 3, ItemData("Sword reflection", 5))

items_sword = [item_sword_strength, item_sword_aimline, item_sword_stab, item_sword_reflection]

item_artillery_mortar: ItemDataCode = ItemDataCode(dome_keeper_index_artillery + 0, ItemData("Artillery mortar", 6))
item_artillery_airgun: ItemDataCode = ItemDataCode(dome_keeper_index_artillery + 1, ItemData("Artillery air gun", 4))

items_artillery = [item_artillery_mortar, item_artillery_airgun]

item_tesla_reticle_speed: ItemDataCode = ItemDataCode(dome_keeper_index_tesla + 0, ItemData("Tesla reticle speed", 4))
item_tesla_quick_shot   : ItemDataCode = ItemDataCode(dome_keeper_index_tesla + 1, ItemData("Tesla quick shot", 2))
item_tesla_shot_power   : ItemDataCode = ItemDataCode(dome_keeper_index_tesla + 2, ItemData("Tesla shot power", 6))
item_tesla_auto_aim     : ItemDataCode = ItemDataCode(dome_keeper_index_tesla + 3, ItemData("Tesla auto aim", 1))
item_tesla_better_orb   : ItemDataCode = ItemDataCode(dome_keeper_index_tesla + 4, ItemData("Tesla better orb", 7))

items_tesla = [
    item_tesla_reticle_speed,
    item_tesla_quick_shot,
    item_tesla_shot_power, 
    item_tesla_auto_aim, 
    item_tesla_better_orb,
]

item_repellent_delay     : ItemDataCode = ItemDataCode(dome_keeper_index_repellent + 0, ItemData("Repellent delay", 3))
item_repellent_special   : ItemDataCode = ItemDataCode(dome_keeper_index_repellent + 1, ItemData("Repellent ability", 3))
item_repellent_overcharge: ItemDataCode = ItemDataCode(dome_keeper_index_repellent + 2, ItemData("Repellent overcharge", 5))

items_repellent = [item_repellent_delay, item_repellent_special, item_repellent_overcharge]

item_shield_strength  : ItemDataCode = ItemDataCode(dome_keeper_index_shield + 0, ItemData("Shield strength", 3))
item_shield_special   : ItemDataCode = ItemDataCode(dome_keeper_index_shield + 1, ItemData("Shield ability", 3))
item_shield_overcharge: ItemDataCode = ItemDataCode(dome_keeper_index_shield + 2, ItemData("Shield overcharge", 3))

items_shield = [item_shield_strength, item_shield_special, item_shield_overcharge]

item_orchard_duration    : ItemDataCode = ItemDataCode(dome_keeper_index_orchard + 0, ItemData("Fruit duration", 3))
item_orchard_overcharge  : ItemDataCode = ItemDataCode(dome_keeper_index_orchard + 1, ItemData("Orchard overcharge", 2))
item_orchard_special     : ItemDataCode = ItemDataCode(dome_keeper_index_orchard + 2, ItemData("Orchard ability", 3))
item_orchard_speed_boost : ItemDataCode = ItemDataCode(dome_keeper_index_orchard + 3, ItemData("Fruit speed boost", 3))
item_orchard_mining_boost: ItemDataCode = ItemDataCode(dome_keeper_index_orchard + 4, ItemData("Fruit mining boost", 3))

items_orchard = [item_orchard_duration, item_orchard_overcharge, item_orchard_special, item_orchard_speed_boost, item_orchard_mining_boost]

item_layer_unlock  : ItemDataCode = ItemDataCode(dome_keeper_index_layers + 0, ItemData("Layer unlock", 6, classification=IC.progression))

def generate_all_items() -> Dict[int, ItemData]:
    rtr: Dict[int, ItemData] = {}
    for idc in items_engineer + items_assessor + items_laser + items_sword + items_artillery + items_tesla + items_shield + items_repellent + items_orchard:
        rtr[idc.code] = idc.data
    rtr[item_layer_unlock.code] = item_layer_unlock.data    
    rtr[item_filler_cobalt.code] = item_filler_cobalt.data
    rtr[item_trap_wavestart.code] = item_trap_wavestart.data
    rtr[item_engineer_drill.code] = item_engineer_drill.data
    rtr[item_assessor_spheres_strength.code] = item_assessor_spheres_strength.data
    rtr[item_assessor_spheres_lifetime.code] = item_assessor_spheres_lifetime.data
    return rtr
