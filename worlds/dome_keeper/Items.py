from BaseClasses import Item, ItemClassification as IC

DOME_KEEPER_ITEM_INDEX = 4242000

class ItemDataCode():
    code: int
    name: str
    classification: IC = IC.useful

    def __init__(self, code: int, name: str, classification: IC = IC.useful):
        self.code = code
        self.name = name
        self.classification = classification

DOME_KEEPER_ITEM_INDEX_ENGINEER = DOME_KEEPER_ITEM_INDEX
DOME_KEEPER_ITEM_INDEX_ASSESSOR = DOME_KEEPER_ITEM_INDEX + 10
DOME_KEEPER_ITEM_INDEX_LASER = DOME_KEEPER_ITEM_INDEX + 20
DOME_KEEPER_ITEM_INDEX_SWORD = DOME_KEEPER_ITEM_INDEX + 30
DOME_KEEPER_ITEM_INDEX_ARTILLERY = DOME_KEEPER_ITEM_INDEX + 40
DOME_KEEPER_ITEM_INDEX_TESLA = DOME_KEEPER_ITEM_INDEX + 50
DOME_KEEPER_ITEM_INDEX_REPELLENT = DOME_KEEPER_ITEM_INDEX + 60
DOME_KEEPER_ITEM_INDEX_SHIELD = DOME_KEEPER_ITEM_INDEX + 70
DOME_KEEPER_ITEM_INDEX_ORCHARD = DOME_KEEPER_ITEM_INDEX + 80
DOME_KEEPER_ITEM_INDEX_DRONEYARD = DOME_KEEPER_ITEM_INDEX + 85
DOME_KEEPER_ITEM_INDEX_COBALT = DOME_KEEPER_ITEM_INDEX + 90
DOME_KEEPER_ITEM_INDEX_TRAP = DOME_KEEPER_ITEM_INDEX + 91
DOME_KEEPER_ITEM_INDEX_LAYERS = DOME_KEEPER_ITEM_INDEX + 100

DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS = DOME_KEEPER_ITEM_INDEX + 200

#region Sync items
item_filler_cobalt: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_COBALT, "Extra cobalt", IC.filler)
item_trap_wavestart: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_TRAP, "Wave start", IC.filler)

# 18 maximum + 
item_engineer_drill  : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ENGINEER + 0, "Drill upgrade", classification=IC.progression) # 10
item_engineer_jetpack: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ENGINEER + 1, "Jetpack upgrade")
item_engineer_carry  : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ENGINEER + 2, "Carry upgrade")

# 43 maximum
item_assessor_movement          : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSESSOR + 0, "Gravitational movement")
item_assessor_spheres_strength  : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSESSOR + 1, "Kinetic spheres", classification=IC.progression) # 10
item_assessor_bundles           : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSESSOR + 2, "Bundles upgrade")
item_assessor_spheres_supply    : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSESSOR + 3, "Sphere supply upgrade")
item_assessor_spheres_lifetime  : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSESSOR + 4, "Sphere lifetime upgrade") # 25
# one of the three upgrade and it's better upgrade
item_assessor_spheres_special   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSESSOR + 5, "Sphere special upgrade")
item_assessor_compression_mining: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSESSOR + 6, "Compression mining upgrade")

# 9
item_laser_strength: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_LASER + 0, "Laser strength")
item_laser_speed   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_LASER + 1, "Laser speed")
item_laser_sight   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_LASER + 2, "Laser sight")

# 14
item_sword_strength  : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_SWORD + 0, "Sword strength")
item_sword_aimline   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_SWORD + 1, "Sword aim line")
item_sword_stab      : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_SWORD + 2, "Sword better stab")
item_sword_reflection: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_SWORD + 3, "Sword reflection")

# 10
item_artillery_mortar: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ARTILLERY + 0, "Artillery mortar")
item_artillery_airgun: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ARTILLERY + 1, "Artillery air gun")

# 20
item_tesla_reticle_speed: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_TESLA + 0, "Tesla reticle speed")
item_tesla_quick_shot   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_TESLA + 1, "Tesla quick shot")
item_tesla_shot_power   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_TESLA + 2, "Tesla shot power")
item_tesla_auto_aim     : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_TESLA + 3, "Tesla auto aim")
item_tesla_better_orb   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_TESLA + 4, "Tesla better orb")

# 11
item_repellent_delay     : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_REPELLENT + 0, "Repellent delay")
item_repellent_special   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_REPELLENT + 1, "Repellent ability")
item_repellent_overcharge: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_REPELLENT + 2, "Repellent overcharge")

# 9
item_shield_strength  : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_SHIELD + 0, "Shield strength")
item_shield_special   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_SHIELD + 1, "Shield ability")
item_shield_overcharge: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_SHIELD + 2, "Shield overcharge")

# 14
item_orchard_duration    : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ORCHARD + 0, "Fruit duration")
item_orchard_overcharge  : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ORCHARD + 1, "Orchard overcharge")
item_orchard_special     : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ORCHARD + 2, "Orchard ability")
item_orchard_speed_boost : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ORCHARD + 3, "Fruit speed boost")
item_orchard_mining_boost: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ORCHARD + 4, "Fruit mining boost")

# 21
item_droneyard_drones    : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_DRONEYARD + 0, "Droneyard drones amount") # 10 max
item_droneyard_speed     : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_DRONEYARD + 1, "Droneyard drone speed")
item_droneyard_special   : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_DRONEYARD + 2, "Droneyard special")
item_droneyard_overcharge: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_DRONEYARD + 3, "Droneyard overcharge")

item_layer_unlock        : ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_LAYERS + 0, "Layer unlock", classification=IC.progression)
#endregion

#region Async items

item_assignment_unlock_showdown:            ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 0 , "Showdown assignment unlock", IC.progression)
item_assignment_unlock_iron_contribution:   ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 1 , "Iron contribution assignment unlock", IC.progression)
item_assignment_unlock_upside_down:         ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 2 , "Upside down assignment unlock", IC.progression)
item_assignment_unlock_maze:                ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 3 , "Maze assignment unlock", IC.progression)
item_assignment_unlock_projectile_hell:     ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 4 , "Projectile hell assignment unlock", IC.progression)
item_assignment_unlock_dense_iron:          ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 5 , "Dense iron assignment unlock", IC.progression)
item_assignment_unlock_barren_lands:        ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 6 , "Barren lands assignment unlock", IC.progression)
item_assignment_unlock_defective_weapon:    ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 7 , "Defective weapon assignment unlock", IC.progression)
item_assignment_unlock_heavy_hitters:       ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 8 , "Heavy hitters assignment unlock", IC.progression)
item_assignment_unlock_swiss_cheese:        ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 9 , "Swiss cheese assignment unlock", IC.progression)
item_assignment_unlock_logistical_problem:  ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 10, "Logistical problem assignment unlock", IC.progression)
item_assignment_unlock_high_risk:           ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 11, "High risk assignment unlock", IC.progression)
item_assignment_unlock_monster_masses:      ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 12, "Monster masses assignment unlock", IC.progression)
item_assignment_unlock_iron_shortage:       ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 13, "Iron shortage assignment unlock", IC.progression)
item_assignment_unlock_mining_problem:      ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 14, "Mining problem assignment unlock", IC.progression)
item_assignment_unlock_cobalt_contribution: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 15, "Cobalt contribution assignment unlock", IC.progression)

item_assignment_starting_iron:   ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 20, "Extra starting iron", IC.filler)
item_assignment_starting_water:  ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 21, "Extra starting water", IC.filler)
item_assignment_starting_cobalt: ItemDataCode = ItemDataCode(DOME_KEEPER_ITEM_INDEX_ASSIGNMENTS + 22, "Extra starting cobalt", IC.filler)

item_assignments = [
    item_assignment_unlock_showdown,
    item_assignment_unlock_iron_contribution,
    item_assignment_unlock_upside_down,     
    item_assignment_unlock_maze,           
    item_assignment_unlock_projectile_hell,
    item_assignment_unlock_dense_iron,      
    item_assignment_unlock_barren_lands,   
    item_assignment_unlock_defective_weapon,
    item_assignment_unlock_heavy_hitters,   
    item_assignment_unlock_swiss_cheese,   
    item_assignment_unlock_logistical_problem,
    item_assignment_unlock_high_risk,        
    item_assignment_unlock_monster_masses,   
    item_assignment_unlock_iron_shortage,
    item_assignment_unlock_mining_problem, 
    item_assignment_unlock_cobalt_contribution
]


#endregion

all_items : list[ItemDataCode] = [
    item_engineer_drill, item_engineer_jetpack,  item_engineer_carry,
    item_assessor_movement, item_assessor_bundles, item_assessor_spheres_supply, item_assessor_spheres_special, item_assessor_compression_mining,
    item_assessor_spheres_strength, item_assessor_spheres_lifetime,
    item_laser_strength, item_laser_speed, item_laser_sight,
    item_sword_strength, item_sword_aimline, item_sword_stab, item_sword_reflection,
    item_artillery_mortar, item_artillery_airgun,
    item_tesla_reticle_speed, item_tesla_quick_shot, item_tesla_shot_power, item_tesla_auto_aim, item_tesla_better_orb,
    item_repellent_delay, item_repellent_special, item_repellent_overcharge,
    item_shield_strength, item_shield_special, item_shield_overcharge,
    item_orchard_duration, item_orchard_overcharge, item_orchard_special, item_orchard_speed_boost, item_orchard_mining_boost,
    item_layer_unlock,
    item_filler_cobalt, item_trap_wavestart,
    item_assignment_unlock_showdown, item_assignment_unlock_iron_contribution, item_assignment_unlock_upside_down, item_assignment_unlock_maze,              
    item_assignment_unlock_projectile_hell, item_assignment_unlock_dense_iron, item_assignment_unlock_barren_lands, item_assignment_unlock_defective_weapon,
    item_assignment_unlock_heavy_hitters, item_assignment_unlock_swiss_cheese, item_assignment_unlock_logistical_problem, item_assignment_unlock_high_risk,
    item_assignment_unlock_monster_masses, item_assignment_unlock_iron_shortage, item_assignment_unlock_mining_problem, item_assignment_unlock_cobalt_contribution,
    item_assignment_starting_iron, item_assignment_starting_water, item_assignment_starting_cobalt
]

def generate_item(player: int, itemDataCode: ItemDataCode) -> Item:
    return Item(itemDataCode.name, itemDataCode.classification, itemDataCode.code, player)

def generate_items(player: int, itemDataCode: ItemDataCode, count: int) -> list[Item]:
    rtr = []
    for _ in range(count):
        rtr.append(generate_item(player, itemDataCode))
    return rtr

def generate_engineer_upgrades(player: int, drill_upgrades: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_engineer_drill,              drill_upgrades))
    rtr.extend(generate_items(player, item_engineer_jetpack,            4))
    rtr.extend(generate_items(player, item_engineer_carry,              4))
    return rtr

def generate_assessor_upgrades(player: int, spheres_strength: int, spheres_lifetime: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_assessor_movement,           4))
    rtr.extend(generate_items(player, item_assessor_bundles,            4))
    rtr.extend(generate_items(player, item_assessor_spheres_supply,     6))
    rtr.extend(generate_items(player, item_assessor_spheres_special,    2))
    rtr.extend(generate_items(player, item_assessor_compression_mining, 2))
    rtr.extend(generate_items(player, item_assessor_spheres_strength,   spheres_strength))
    rtr.extend(generate_items(player, item_assessor_spheres_lifetime,   spheres_lifetime))
    return rtr

def generate_laser_upgrades(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_laser_strength,              4))
    rtr.extend(generate_items(player, item_laser_speed,                 4))
    rtr.extend(generate_items(player, item_laser_sight,                 6))
    return rtr

def generate_sword_upgrades(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_sword_strength,              4))
    rtr.extend(generate_items(player, item_sword_aimline,               1))
    rtr.extend(generate_items(player, item_sword_stab,                  4))
    rtr.extend(generate_items(player, item_sword_reflection,            5))
    return rtr

def generate_artillery_upgrades(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_artillery_mortar,            6))
    rtr.extend(generate_items(player, item_artillery_airgun,            4))
    return rtr

def generate_tesla_upgrades(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_tesla_reticle_speed,         4))
    rtr.extend(generate_items(player, item_tesla_quick_shot,            2))
    rtr.extend(generate_items(player, item_tesla_shot_power,            6))
    rtr.extend(generate_items(player, item_tesla_auto_aim,              1))
    rtr.extend(generate_items(player, item_tesla_better_orb,            7))
    return rtr

def generate_repellent_upgrades(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_repellent_delay,             3))
    rtr.extend(generate_items(player, item_repellent_special,           3))
    rtr.extend(generate_items(player, item_repellent_overcharge,        5))
    return rtr

def generate_shield_upgrades(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_shield_strength  ,           3))
    rtr.extend(generate_items(player, item_shield_special   ,           3))
    rtr.extend(generate_items(player, item_shield_overcharge,           3))
    return rtr

def generate_orchard_upgrades(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_orchard_duration    ,        3))
    rtr.extend(generate_items(player, item_orchard_overcharge  ,        2))
    rtr.extend(generate_items(player, item_orchard_special     ,        3))
    rtr.extend(generate_items(player, item_orchard_speed_boost ,        3))
    rtr.extend(generate_items(player, item_orchard_mining_boost,        3))
    return rtr

def generate_droneyard_upgrades(player: int, drones_amount: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.extend(generate_items(player, item_droneyard_drones    ,        drones_amount))
    rtr.extend(generate_items(player, item_droneyard_speed     ,        5))
    rtr.extend(generate_items(player, item_droneyard_special   ,        3))
    rtr.extend(generate_items(player, item_droneyard_overcharge,        3))
    return rtr

def generate_layers_upgrades(player: int, layers_amount: int) -> list[Item]:
    rtr: list[Item] = generate_items(player, item_layer_unlock, layers_amount)
    return rtr

def generate_cobalt_upgrades(player: int, cobalt_amount: int) -> list[Item]:
    rtr: list[Item] = generate_items(player, item_filler_cobalt, cobalt_amount)
    return rtr

def generate_unlocks(player: int) -> list[Item]:
    rtr: list[Item] = []
    rtr.append(generate_item(player, item_assignment_unlock_showdown           ))
    rtr.append(generate_item(player, item_assignment_unlock_iron_contribution  ))
    rtr.append(generate_item(player, item_assignment_unlock_upside_down        ))
    rtr.append(generate_item(player, item_assignment_unlock_maze               ))
    rtr.append(generate_item(player, item_assignment_unlock_projectile_hell    ))
    rtr.append(generate_item(player, item_assignment_unlock_dense_iron         ))
    rtr.append(generate_item(player, item_assignment_unlock_barren_lands       ))
    rtr.append(generate_item(player, item_assignment_unlock_defective_weapon   ))
    rtr.append(generate_item(player, item_assignment_unlock_heavy_hitters      ))
    rtr.append(generate_item(player, item_assignment_unlock_swiss_cheese       ))
    rtr.append(generate_item(player, item_assignment_unlock_logistical_problem ))
    rtr.append(generate_item(player, item_assignment_unlock_high_risk          ))
    rtr.append(generate_item(player, item_assignment_unlock_monster_masses     ))
    rtr.append(generate_item(player, item_assignment_unlock_iron_shortage      ))
    rtr.append(generate_item(player, item_assignment_unlock_mining_problem     ))
    rtr.append(generate_item(player, item_assignment_unlock_cobalt_contribution))
    return rtr

def generate_iron_rewards(player: int, iron_amount: int) -> list[Item]:
    return generate_items(player, item_assignment_starting_iron, iron_amount)

def generate_water_rewards(player: int, water_amount: int) -> list[Item]:
    return generate_items(player, item_assignment_starting_water, water_amount)

def generate_cobalt_rewards(player: int, cobalt_amount: int) -> list[Item]:
    return generate_items(player, item_assignment_starting_cobalt, cobalt_amount)

def generate_all_upgrades(
        player: int,
        drill_upgrades: int,
        spheres_strength: int,
        spheres_lifetime: int,
        drones_amount: int,
        layers_amount: int,
        cobalt_amount: int,
        iron_rewards: int,
        water_rewards: int,
        cobalt_rewards: int) -> list[Item]:
    rtr = []
    rtr += generate_engineer_upgrades(player, drill_upgrades)
    rtr += generate_assessor_upgrades(player, spheres_strength, spheres_lifetime)
    rtr += generate_laser_upgrades(player)
    rtr += generate_sword_upgrades(player)
    rtr += generate_artillery_upgrades(player)
    rtr += generate_tesla_upgrades(player)
    rtr += generate_repellent_upgrades(player)
    rtr += generate_shield_upgrades(player)
    rtr += generate_orchard_upgrades(player)
    rtr += generate_droneyard_upgrades(player, drones_amount)
    rtr += generate_layers_upgrades(player, layers_amount)
    rtr += generate_cobalt_upgrades(player, cobalt_amount)
    rtr += generate_unlocks(player)
    rtr += generate_iron_rewards(player, iron_rewards)
    rtr += generate_water_rewards(player, water_rewards)
    rtr += generate_cobalt_rewards(player, cobalt_rewards)
    return rtr