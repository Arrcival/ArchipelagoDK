class DomeKeeperLocationData():
    name: str
    code: int

    def __init__(self, name: str, code: int):
        self.name = name
        self.code = code

DOME_KEEPER_LOCATION_INDEX = 4243000


UPGRADE_FIRST_ID              = DOME_KEEPER_LOCATION_INDEX + 0
CAVE_FIRST_ID                 = DOME_KEEPER_LOCATION_INDEX + 20
ASSIGNMENT_FIRST_ID           = DOME_KEEPER_LOCATION_INDEX + 30
ASSIGNMENT_CHALLENGE_FIRST_ID = DOME_KEEPER_LOCATION_INDEX + 50
ARTIFACT_SYNC_FIRST_ID        = DOME_KEEPER_LOCATION_INDEX + 70
ARTIFACT_ASYNC_FIRST_ID       = DOME_KEEPER_LOCATION_INDEX + 80
SWITCHES_FIRST_ID             = DOME_KEEPER_LOCATION_INDEX + 201

LAYERS_MAX_AMOUNT = 7

UPGRADES_LOCATIONS_AMOUNT = 12

LAYER_OFFSET = 100

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

location_assignment_showdown_artifact_1 =            DomeKeeperLocationData("Showdown regular - Artifact 1",    ARTIFACT_ASYNC_FIRST_ID + 0 )
location_assignment_iron_contribution_artifact_1 =   DomeKeeperLocationData("Iron contribution - Artifact 1",   ARTIFACT_ASYNC_FIRST_ID + 1 )
location_assignment_upside_down_artifact_1 =         DomeKeeperLocationData("Upside down - Artifact 1",         ARTIFACT_ASYNC_FIRST_ID + 2 )
location_assignment_maze_artifact_1 =                DomeKeeperLocationData("Maze regular - Artifact 1",        ARTIFACT_ASYNC_FIRST_ID + 3 )
location_assignment_projectile_hell_artifact_1 =     DomeKeeperLocationData("Projectile hell - Artifact 1",     ARTIFACT_ASYNC_FIRST_ID + 4 )
location_assignment_dense_iron_artifact_1 =          DomeKeeperLocationData("Dense iron  - Artifact 1",         ARTIFACT_ASYNC_FIRST_ID + 5 )
location_assignment_barren_lands_artifact_1 =        DomeKeeperLocationData("Barren lands - Artifact 1",        ARTIFACT_ASYNC_FIRST_ID + 6 )
location_assignment_defective_weapon_artifact_1 =    DomeKeeperLocationData("Defective weapon - Artifact 1",    ARTIFACT_ASYNC_FIRST_ID + 7 )
location_assignment_heavy_hitters_artifact_1 =       DomeKeeperLocationData("Heavy hitters - Artifact 1",       ARTIFACT_ASYNC_FIRST_ID + 8 )
location_assignment_swiss_cheese_artifact_1 =        DomeKeeperLocationData("Swiss cheese - Artifact 1",        ARTIFACT_ASYNC_FIRST_ID + 9 )
location_assignment_logistical_problem_artifact_1 =  DomeKeeperLocationData("Logistical problem - Artifact 1",  ARTIFACT_ASYNC_FIRST_ID + 10)
location_assignment_high_risk_artifact_1 =           DomeKeeperLocationData("High risk - Artifact 1",           ARTIFACT_ASYNC_FIRST_ID + 11)
location_assignment_monster_masses_artifact_1 =      DomeKeeperLocationData("Monster masses - Artifact 1",      ARTIFACT_ASYNC_FIRST_ID + 12)
location_assignment_iron_shortage_artifact_1 =       DomeKeeperLocationData("Iron shortage - Artifact 1",       ARTIFACT_ASYNC_FIRST_ID + 13)
location_assignment_mining_problem_artifact_1 =      DomeKeeperLocationData("Mining problem - Artifact 1",      ARTIFACT_ASYNC_FIRST_ID + 14)
location_assignment_cobalt_contribution_artifact_1 = DomeKeeperLocationData("Cobalt contribution - Artifact 1", ARTIFACT_ASYNC_FIRST_ID + 15)
location_assignment_showdown_artifact_2 =            DomeKeeperLocationData("Showdown regular - Artifact 2",    ARTIFACT_ASYNC_FIRST_ID + 16 + 0 )
location_assignment_iron_contribution_artifact_2 =   DomeKeeperLocationData("Iron contribution - Artifact 2",   ARTIFACT_ASYNC_FIRST_ID + 16 + 1 )
location_assignment_upside_down_artifact_2 =         DomeKeeperLocationData("Upside down - Artifact 2",         ARTIFACT_ASYNC_FIRST_ID + 16 + 2 )
location_assignment_maze_artifact_2 =                DomeKeeperLocationData("Maze regular - Artifact 2",        ARTIFACT_ASYNC_FIRST_ID + 16 + 3 )
location_assignment_projectile_hell_artifact_2 =     DomeKeeperLocationData("Projectile hell - Artifact 2",     ARTIFACT_ASYNC_FIRST_ID + 16 + 4 )
location_assignment_dense_iron_artifact_2 =          DomeKeeperLocationData("Dense iron  - Artifact 2",         ARTIFACT_ASYNC_FIRST_ID + 16 + 5 )
location_assignment_barren_lands_artifact_2 =        DomeKeeperLocationData("Barren lands - Artifact 2",        ARTIFACT_ASYNC_FIRST_ID + 16 + 6 )
location_assignment_defective_weapon_artifact_2 =    DomeKeeperLocationData("Defective weapon - Artifact 2",    ARTIFACT_ASYNC_FIRST_ID + 16 + 7 )
location_assignment_heavy_hitters_artifact_2 =       DomeKeeperLocationData("Heavy hitters - Artifact 2",       ARTIFACT_ASYNC_FIRST_ID + 16 + 8 )
location_assignment_swiss_cheese_artifact_2 =        DomeKeeperLocationData("Swiss cheese - Artifact 2",        ARTIFACT_ASYNC_FIRST_ID + 16 + 9 )
location_assignment_logistical_problem_artifact_2 =  DomeKeeperLocationData("Logistical problem - Artifact 2",  ARTIFACT_ASYNC_FIRST_ID + 16 + 10)
location_assignment_high_risk_artifact_2 =           DomeKeeperLocationData("High risk - Artifact 2",           ARTIFACT_ASYNC_FIRST_ID + 16 + 11)
location_assignment_monster_masses_artifact_2 =      DomeKeeperLocationData("Monster masses - Artifact 2",      ARTIFACT_ASYNC_FIRST_ID + 16 + 12)
location_assignment_iron_shortage_artifact_2 =       DomeKeeperLocationData("Iron shortage - Artifact 2",       ARTIFACT_ASYNC_FIRST_ID + 16 + 13)
location_assignment_mining_problem_artifact_2 =      DomeKeeperLocationData("Mining problem - Artifact 2",      ARTIFACT_ASYNC_FIRST_ID + 16 + 14)
location_assignment_cobalt_contribution_artifact_2 = DomeKeeperLocationData("Cobalt contribution - Artifact 2", ARTIFACT_ASYNC_FIRST_ID + 16 + 15)

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

location_assignments_first_artifact : list[DomeKeeperLocationData] = [
    location_assignment_showdown_artifact_1,     
    location_assignment_iron_contribution_artifact_1,
    location_assignment_upside_down_artifact_1,     
    location_assignment_maze_artifact_1,          
    location_assignment_projectile_hell_artifact_1,
    location_assignment_dense_iron_artifact_1,    
    location_assignment_barren_lands_artifact_1,  
    location_assignment_defective_weapon_artifact_1,
    location_assignment_heavy_hitters_artifact_1,  
    location_assignment_swiss_cheese_artifact_1,   
    location_assignment_logistical_problem_artifact_1,
    location_assignment_high_risk_artifact_1,        
    location_assignment_monster_masses_artifact_1,  
    location_assignment_iron_shortage_artifact_1,   
    location_assignment_mining_problem_artifact_1,  
    location_assignment_cobalt_contribution_artifact_1
]

location_assignments_second_artifact : list[DomeKeeperLocationData] = [
    location_assignment_showdown_artifact_2,     
    location_assignment_iron_contribution_artifact_2,
    location_assignment_upside_down_artifact_2,     
    location_assignment_maze_artifact_2,          
    location_assignment_projectile_hell_artifact_2,
    location_assignment_dense_iron_artifact_2,    
    location_assignment_barren_lands_artifact_2,  
    location_assignment_defective_weapon_artifact_2,
    location_assignment_heavy_hitters_artifact_2,  
    location_assignment_swiss_cheese_artifact_2,   
    location_assignment_logistical_problem_artifact_2,
    location_assignment_high_risk_artifact_2,        
    location_assignment_monster_masses_artifact_2,  
    location_assignment_iron_shortage_artifact_2,   
    location_assignment_mining_problem_artifact_2,  
    location_assignment_cobalt_contribution_artifact_2
]
#endregion

def generate_locations_data() -> list[DomeKeeperLocationData] :
    rtr: list[DomeKeeperLocationData] = []
    rtr.extend(location_table_easy_upgrades.copy())
    rtr.extend(location_table_normal_upgrades.copy())
    rtr.extend(location_table_hard_upgrades.copy())
    rtr.extend(location_assignments_regular.copy())
    rtr.extend(location_assignments_challenge.copy())
    rtr.extend(location_assignments_first_artifact.copy())
    rtr.extend(location_assignments_second_artifact.copy())
    rtr.extend(generate_switches_locations())
    rtr.extend(generate_caves_locations())
    rtr.extend(generate_artifacts_locations())
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

def generate_artifacts_locations() -> list[DomeKeeperLocationData] :
    rtr = []
    for i in range(LAYERS_MAX_AMOUNT):
        rtr.append(DomeKeeperLocationData("Layer " + str(i + 1) + " - Artifact", ARTIFACT_SYNC_FIRST_ID + i))
    return rtr

def get_layers_amount_from_map_size(map_size: int) -> int:
    layers = map_size + 3
    if map_size >= 2:
        layers += 1
    return layers

def get_non_switch_location_count(map_size: int) -> int:
    """Count locations that are never switch-locations for Relic Hunt modes."""
    layers = get_layers_amount_from_map_size(map_size)

    upgrades_count = (
        len(location_table_easy_upgrades)
        + len(location_table_normal_upgrades)
        + len(location_table_hard_upgrades)
    )
    caves_count = layers
    artifacts_count = layers

    return upgrades_count + caves_count + artifacts_count