class DomeKeeperLocationData():
    name: str
    code: int

    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code

DOME_KEEPER_LOCATION_INDEX = 4243000


CAVE_FIRST_ID = DOME_KEEPER_LOCATION_INDEX + 20
LAYERS_MAX_AMOUNT = 7

ASSIGNMENT_FIRST_ID = DOME_KEEPER_LOCATION_INDEX + 30
ASSIGNMENT_CHALLENGE_FIRST_ID = DOME_KEEPER_LOCATION_INDEX + 50

UPGRADES_LOCATIONS_AMOUNT = 12

SWITCHES_FIRST_ID = DOME_KEEPER_LOCATION_INDEX + 101

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

#region Assignments completions
location_assignment_completion_regular_showdown =              DomeKeeperLocationData("Showdown regular completion",              ASSIGNMENT_FIRST_ID + 0 )
location_assignment_completion_regular_iron_contribution =     DomeKeeperLocationData("Iron contribution regular completion",     ASSIGNMENT_FIRST_ID + 1 )
location_assignment_completion_regular_upside_down =           DomeKeeperLocationData("Upside down regular completion",           ASSIGNMENT_FIRST_ID + 2 )
location_assignment_completion_regular_maze =                  DomeKeeperLocationData("Maze regular completion",                  ASSIGNMENT_FIRST_ID + 3 )
location_assignment_completion_regular_projectile_hell =       DomeKeeperLocationData("Projectile hell regular completion",       ASSIGNMENT_FIRST_ID + 4 )
location_assignment_completion_regular_dense_iron =            DomeKeeperLocationData("Dense iron regular completion",            ASSIGNMENT_FIRST_ID + 5 )
location_assignment_completion_regular_barren_lands =          DomeKeeperLocationData("Barren lands regular completion",          ASSIGNMENT_FIRST_ID + 6 )
location_assignment_completion_regular_defective_weapon =      DomeKeeperLocationData("Defective weapon regular completion",      ASSIGNMENT_FIRST_ID + 7 )
location_assignment_completion_regular_heavy_hitters =         DomeKeeperLocationData("Heavy hitters regular completion",         ASSIGNMENT_FIRST_ID + 8 )
location_assignment_completion_regular_swiss_cheese =          DomeKeeperLocationData("Swiss cheese regular completion",          ASSIGNMENT_FIRST_ID + 9 )
location_assignment_completion_regular_logistical_problem =    DomeKeeperLocationData("Logistical problem regular completion",    ASSIGNMENT_FIRST_ID + 10)
location_assignment_completion_regular_high_risk =             DomeKeeperLocationData("High risk regular completion",             ASSIGNMENT_FIRST_ID + 11)
location_assignment_completion_regular_monster_masses =        DomeKeeperLocationData("Monster masses regular completion",        ASSIGNMENT_FIRST_ID + 12)
location_assignment_completion_regular_iron_shortage =         DomeKeeperLocationData("Iron shortage regular completion",         ASSIGNMENT_FIRST_ID + 13)
location_assignment_completion_regular_mining_problem =        DomeKeeperLocationData("Mining problem regular completion",        ASSIGNMENT_FIRST_ID + 14)
location_assignment_completion_regular_cobalt_contribution =   DomeKeeperLocationData("Cobalt contribution regular completion",   ASSIGNMENT_FIRST_ID + 15)
location_assignment_completion_challenge_showdown =            DomeKeeperLocationData("Showdown challenge completion",            ASSIGNMENT_CHALLENGE_FIRST_ID + 0 )
location_assignment_completion_challenge_iron_contribution =   DomeKeeperLocationData("Iron contribution challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 1 )
location_assignment_completion_challenge_upside_down =         DomeKeeperLocationData("Upside down challenge completion",         ASSIGNMENT_CHALLENGE_FIRST_ID + 2 )
location_assignment_completion_challenge_maze =                DomeKeeperLocationData("Maze challenge completion",                ASSIGNMENT_CHALLENGE_FIRST_ID + 3 )
location_assignment_completion_challenge_projectile_hell =     DomeKeeperLocationData("Projectile hell challenge completion",     ASSIGNMENT_CHALLENGE_FIRST_ID + 4 )
location_assignment_completion_challenge_dense_iron =          DomeKeeperLocationData("Dense iron challenge completion",          ASSIGNMENT_CHALLENGE_FIRST_ID + 5 )
location_assignment_completion_challenge_barren_lands =        DomeKeeperLocationData("Barren lands challenge completion",        ASSIGNMENT_CHALLENGE_FIRST_ID + 6 )
location_assignment_completion_challenge_defective_weapon =    DomeKeeperLocationData("Defective weapon challenge completion",    ASSIGNMENT_CHALLENGE_FIRST_ID + 7 )
location_assignment_completion_challenge_heavy_hitters =       DomeKeeperLocationData("Heavy hitters challenge completion",       ASSIGNMENT_CHALLENGE_FIRST_ID + 8 )
location_assignment_completion_challenge_swiss_cheese =        DomeKeeperLocationData("Swiss cheese challenge completion",        ASSIGNMENT_CHALLENGE_FIRST_ID + 9 )
location_assignment_completion_challenge_logistical_problem =  DomeKeeperLocationData("Logistical problem challenge completion",  ASSIGNMENT_CHALLENGE_FIRST_ID + 10)
location_assignment_completion_challenge_high_risk =           DomeKeeperLocationData("High risk challenge completion",           ASSIGNMENT_CHALLENGE_FIRST_ID + 11)
location_assignment_completion_challenge_monster_masses =      DomeKeeperLocationData("Monster masses challenge completion",      ASSIGNMENT_CHALLENGE_FIRST_ID + 12)
location_assignment_completion_challenge_iron_shortage =       DomeKeeperLocationData("Iron shortage challenge completion",       ASSIGNMENT_CHALLENGE_FIRST_ID + 13)
location_assignment_completion_challenge_mining_problem =      DomeKeeperLocationData("Mining problem challenge completion",      ASSIGNMENT_CHALLENGE_FIRST_ID + 14)
location_assignment_completion_challenge_cobalt_contribution=  DomeKeeperLocationData("Cobalt contribution challenge completion", ASSIGNMENT_CHALLENGE_FIRST_ID + 15)

location_assignments_regular : list[DomeKeeperLocationData] = [
    location_assignment_completion_regular_showdown,      
    location_assignment_completion_regular_iron_contribution,
    location_assignment_completion_regular_upside_down,       
    location_assignment_completion_regular_maze,             
    location_assignment_completion_regular_projectile_hell,
    location_assignment_completion_regular_dense_iron,     
    location_assignment_completion_regular_barren_lands,  
    location_assignment_completion_regular_defective_weapon, 
    location_assignment_completion_regular_heavy_hitters,   
    location_assignment_completion_regular_swiss_cheese,   
    location_assignment_completion_regular_logistical_problem,
    location_assignment_completion_regular_high_risk,    
    location_assignment_completion_regular_monster_masses,  
    location_assignment_completion_regular_iron_shortage,  
    location_assignment_completion_regular_mining_problem,
    location_assignment_completion_regular_cobalt_contribution
]

location_assignments_challenge : list[DomeKeeperLocationData] = [
    location_assignment_completion_challenge_showdown,      
    location_assignment_completion_challenge_iron_contribution,
    location_assignment_completion_challenge_upside_down,       
    location_assignment_completion_challenge_maze,             
    location_assignment_completion_challenge_projectile_hell,
    location_assignment_completion_challenge_dense_iron,     
    location_assignment_completion_challenge_barren_lands,  
    location_assignment_completion_challenge_defective_weapon, 
    location_assignment_completion_challenge_heavy_hitters,   
    location_assignment_completion_challenge_swiss_cheese,   
    location_assignment_completion_challenge_logistical_problem,
    location_assignment_completion_challenge_high_risk,    
    location_assignment_completion_challenge_monster_masses,  
    location_assignment_completion_challenge_iron_shortage,  
    location_assignment_completion_challenge_mining_problem,
    location_assignment_completion_challenge_cobalt_contribution
]
#endregion

def generate_locations_data() -> list[DomeKeeperLocationData] :
    rtr: list[DomeKeeperLocationData] = []
    rtr.extend(location_table_easy_upgrades.copy())
    rtr.extend(location_table_normal_upgrades.copy())
    rtr.extend(location_table_hard_upgrades.copy())
    rtr.extend(location_assignments_regular.copy())
    rtr.extend(location_assignments_challenge.copy())
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