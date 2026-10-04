from .Utils import ASSIGNMENTS_AMOUNT

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
ASSIGNMENT_CHALLENGE_FIRST_ID = DOME_KEEPER_LOCATION_INDEX + 60
TREASURE_SYNC_FIRST_ID        = DOME_KEEPER_LOCATION_INDEX + 90
TREASURE_ASYNC_FIRST_ID       = DOME_KEEPER_LOCATION_INDEX + 100
SWITCHES_FIRST_ID             = DOME_KEEPER_LOCATION_INDEX + 301

LAYERS_MAX_AMOUNT = 10

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
location_assignment_completion_regular_showdown =                DomeKeeperLocationData("Showdown regular completion",              ASSIGNMENT_FIRST_ID + 0 )
location_assignment_completion_regular_iron_contribution =       DomeKeeperLocationData("Iron contribution regular completion",     ASSIGNMENT_FIRST_ID + 1 )
location_assignment_completion_regular_upside_down =             DomeKeeperLocationData("Upside down regular completion",           ASSIGNMENT_FIRST_ID + 2 )
location_assignment_completion_regular_maze =                    DomeKeeperLocationData("Maze regular completion",                  ASSIGNMENT_FIRST_ID + 3 )
location_assignment_completion_regular_projectile_hell =         DomeKeeperLocationData("Projectile hell regular completion",       ASSIGNMENT_FIRST_ID + 4 )
location_assignment_completion_regular_dense_iron =              DomeKeeperLocationData("Dense iron regular completion",            ASSIGNMENT_FIRST_ID + 5 )
location_assignment_completion_regular_barren_lands =            DomeKeeperLocationData("Barren lands regular completion",          ASSIGNMENT_FIRST_ID + 6 )
location_assignment_completion_regular_defective_weapon =        DomeKeeperLocationData("Defective weapon regular completion",      ASSIGNMENT_FIRST_ID + 7 )
location_assignment_completion_regular_heavy_hitters =           DomeKeeperLocationData("Heavy hitters regular completion",         ASSIGNMENT_FIRST_ID + 8 )
location_assignment_completion_regular_swiss_cheese =            DomeKeeperLocationData("Swiss cheese regular completion",          ASSIGNMENT_FIRST_ID + 9 )
location_assignment_completion_regular_logistical_problem =      DomeKeeperLocationData("Logistical problem regular completion",    ASSIGNMENT_FIRST_ID + 10)
location_assignment_completion_regular_high_risk =               DomeKeeperLocationData("High risk regular completion",             ASSIGNMENT_FIRST_ID + 11)
location_assignment_completion_regular_monster_masses =          DomeKeeperLocationData("Monster masses regular completion",        ASSIGNMENT_FIRST_ID + 12)
location_assignment_completion_regular_iron_shortage =           DomeKeeperLocationData("Iron shortage regular completion",         ASSIGNMENT_FIRST_ID + 13)
location_assignment_completion_regular_mining_problem =          DomeKeeperLocationData("Mining problem regular completion",        ASSIGNMENT_FIRST_ID + 14)
location_assignment_completion_regular_cobalt_contribution =     DomeKeeperLocationData("Cobalt contribution regular completion",   ASSIGNMENT_FIRST_ID + 15)
location_assignment_completion_regular_broken_comms =            DomeKeeperLocationData("Broken comms regular completion",   ASSIGNMENT_FIRST_ID + 16)
location_assignment_completion_regular_darkness =                DomeKeeperLocationData("Darkness regular completion",   ASSIGNMENT_FIRST_ID + 17)
location_assignment_completion_regular_tree_farm =               DomeKeeperLocationData("Tree farm regular completion",   ASSIGNMENT_FIRST_ID + 18)
location_assignment_completion_regular_acid_rain =               DomeKeeperLocationData("Acid rain regular completion",   ASSIGNMENT_FIRST_ID + 19)
location_assignment_completion_regular_hazardous_iron =          DomeKeeperLocationData("Hazardous iron regular completion",   ASSIGNMENT_FIRST_ID + 20)
location_assignment_completion_regular_emergency =               DomeKeeperLocationData("Emergency regular completion",   ASSIGNMENT_FIRST_ID + 21)
location_assignment_completion_regular_brutal_monsters =         DomeKeeperLocationData("Brutal monsters regular completion",   ASSIGNMENT_FIRST_ID + 22)
location_assignment_completion_regular_logistical_nightmare =    DomeKeeperLocationData("Logistical nightmare regular completion",   ASSIGNMENT_FIRST_ID + 23)
location_assignment_completion_regular_survival_of_the_fittest = DomeKeeperLocationData("Survival of the fittest regular completion",   ASSIGNMENT_FIRST_ID + 24)

location_assignment_completion_challenge_showdown =                DomeKeeperLocationData("Showdown challenge completion",            ASSIGNMENT_CHALLENGE_FIRST_ID + 0 )
location_assignment_completion_challenge_iron_contribution =       DomeKeeperLocationData("Iron contribution challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 1 )
location_assignment_completion_challenge_upside_down =             DomeKeeperLocationData("Upside down challenge completion",         ASSIGNMENT_CHALLENGE_FIRST_ID + 2 )
location_assignment_completion_challenge_maze =                    DomeKeeperLocationData("Maze challenge completion",                ASSIGNMENT_CHALLENGE_FIRST_ID + 3 )
location_assignment_completion_challenge_projectile_hell =         DomeKeeperLocationData("Projectile hell challenge completion",     ASSIGNMENT_CHALLENGE_FIRST_ID + 4 )
location_assignment_completion_challenge_dense_iron =              DomeKeeperLocationData("Dense iron challenge completion",          ASSIGNMENT_CHALLENGE_FIRST_ID + 5 )
location_assignment_completion_challenge_barren_lands =            DomeKeeperLocationData("Barren lands challenge completion",        ASSIGNMENT_CHALLENGE_FIRST_ID + 6 )
location_assignment_completion_challenge_defective_weapon =        DomeKeeperLocationData("Defective weapon challenge completion",    ASSIGNMENT_CHALLENGE_FIRST_ID + 7 )
location_assignment_completion_challenge_heavy_hitters =           DomeKeeperLocationData("Heavy hitters challenge completion",       ASSIGNMENT_CHALLENGE_FIRST_ID + 8 )
location_assignment_completion_challenge_swiss_cheese =            DomeKeeperLocationData("Swiss cheese challenge completion",        ASSIGNMENT_CHALLENGE_FIRST_ID + 9 )
location_assignment_completion_challenge_logistical_problem =      DomeKeeperLocationData("Logistical problem challenge completion",  ASSIGNMENT_CHALLENGE_FIRST_ID + 10)
location_assignment_completion_challenge_high_risk =               DomeKeeperLocationData("High risk challenge completion",           ASSIGNMENT_CHALLENGE_FIRST_ID + 11)
location_assignment_completion_challenge_monster_masses =          DomeKeeperLocationData("Monster masses challenge completion",      ASSIGNMENT_CHALLENGE_FIRST_ID + 12)
location_assignment_completion_challenge_iron_shortage =           DomeKeeperLocationData("Iron shortage challenge completion",       ASSIGNMENT_CHALLENGE_FIRST_ID + 13)
location_assignment_completion_challenge_mining_problem =          DomeKeeperLocationData("Mining problem challenge completion",      ASSIGNMENT_CHALLENGE_FIRST_ID + 14)
location_assignment_completion_challenge_cobalt_contribution=      DomeKeeperLocationData("Cobalt contribution challenge completion", ASSIGNMENT_CHALLENGE_FIRST_ID + 15)
location_assignment_completion_challenge_broken_comms =            DomeKeeperLocationData("Broken comms challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 16)
location_assignment_completion_challenge_darkness =                DomeKeeperLocationData("Darkness challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 17)
location_assignment_completion_challenge_tree_farm =               DomeKeeperLocationData("Tree farm challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 18)
location_assignment_completion_challenge_acid_rain =               DomeKeeperLocationData("Acid rain challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 19)
location_assignment_completion_challenge_hazardous_iron =          DomeKeeperLocationData("Hazardous iron challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 20)
location_assignment_completion_challenge_emergency =               DomeKeeperLocationData("Emergency challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 21)
location_assignment_completion_challenge_brutal_monsters =         DomeKeeperLocationData("Brutal monsters challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 22)
location_assignment_completion_challenge_logistical_nightmare =    DomeKeeperLocationData("Logistical nightmare challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 23)
location_assignment_completion_challenge_survival_of_the_fittest = DomeKeeperLocationData("Survival of the fittest challenge completion",   ASSIGNMENT_CHALLENGE_FIRST_ID + 24)

location_assignment_showdown_treasure_1 =            DomeKeeperLocationData("Showdown regular - Treasure 1",    TREASURE_ASYNC_FIRST_ID + 0 )
location_assignment_iron_contribution_treasure_1 =   DomeKeeperLocationData("Iron contribution - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 1 )
location_assignment_upside_down_treasure_1 =         DomeKeeperLocationData("Upside down - Treasure 1",         TREASURE_ASYNC_FIRST_ID + 2 )
location_assignment_maze_treasure_1 =                DomeKeeperLocationData("Maze regular - Treasure 1",        TREASURE_ASYNC_FIRST_ID + 3 )
location_assignment_projectile_hell_treasure_1 =     DomeKeeperLocationData("Projectile hell - Treasure 1",     TREASURE_ASYNC_FIRST_ID + 4 )
location_assignment_dense_iron_treasure_1 =          DomeKeeperLocationData("Dense iron  - Treasure 1",         TREASURE_ASYNC_FIRST_ID + 5 )
location_assignment_barren_lands_treasure_1 =        DomeKeeperLocationData("Barren lands - Treasure 1",        TREASURE_ASYNC_FIRST_ID + 6 )
location_assignment_defective_weapon_treasure_1 =    DomeKeeperLocationData("Defective weapon - Treasure 1",    TREASURE_ASYNC_FIRST_ID + 7 )
location_assignment_heavy_hitters_treasure_1 =       DomeKeeperLocationData("Heavy hitters - Treasure 1",       TREASURE_ASYNC_FIRST_ID + 8 )
location_assignment_swiss_cheese_treasure_1 =        DomeKeeperLocationData("Swiss cheese - Treasure 1",        TREASURE_ASYNC_FIRST_ID + 9 )
location_assignment_logistical_problem_treasure_1 =  DomeKeeperLocationData("Logistical problem - Treasure 1",  TREASURE_ASYNC_FIRST_ID + 10)
location_assignment_high_risk_treasure_1 =           DomeKeeperLocationData("High risk - Treasure 1",           TREASURE_ASYNC_FIRST_ID + 11)
location_assignment_monster_masses_treasure_1 =      DomeKeeperLocationData("Monster masses - Treasure 1",      TREASURE_ASYNC_FIRST_ID + 12)
location_assignment_iron_shortage_treasure_1 =       DomeKeeperLocationData("Iron shortage - Treasure 1",       TREASURE_ASYNC_FIRST_ID + 13)
location_assignment_mining_problem_treasure_1 =      DomeKeeperLocationData("Mining problem - Treasure 1",      TREASURE_ASYNC_FIRST_ID + 14)
location_assignment_cobalt_contribution_treasure_1 = DomeKeeperLocationData("Cobalt contribution - Treasure 1", TREASURE_ASYNC_FIRST_ID + 15)
location_assignment_broken_comms_treasure_1 =            DomeKeeperLocationData("Broken comms - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 16)
location_assignment_darkness_treasure_1 =                DomeKeeperLocationData("Darkness - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 17)
location_assignment_tree_farm_treasure_1 =               DomeKeeperLocationData("Tree farm - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 18)
location_assignment_acid_rain_treasure_1 =               DomeKeeperLocationData("Acid rain - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 19)
location_assignment_hazardous_iron_treasure_1 =          DomeKeeperLocationData("Hazardous - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 20)
location_assignment_emergency_treasure_1 =               DomeKeeperLocationData("Emergency - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 21)
location_assignment_brutal_monsters_treasure_1 =         DomeKeeperLocationData("Brutal monsters - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 22)
location_assignment_logistical_nightmare_treasure_1 =    DomeKeeperLocationData("Logistical - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 23)
location_assignment_survival_of_the_fittest_treasure_1 = DomeKeeperLocationData("Survival of the fittest - Treasure 1",   TREASURE_ASYNC_FIRST_ID + 24)



location_assignment_showdown_treasure_2 =            DomeKeeperLocationData("Showdown regular - Treasure 2",    TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 0 )
location_assignment_iron_contribution_treasure_2 =   DomeKeeperLocationData("Iron contribution - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 1 )
location_assignment_upside_down_treasure_2 =         DomeKeeperLocationData("Upside down - Treasure 2",         TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 2 )
location_assignment_maze_treasure_2 =                DomeKeeperLocationData("Maze regular - Treasure 2",        TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 3 )
location_assignment_projectile_hell_treasure_2 =     DomeKeeperLocationData("Projectile hell - Treasure 2",     TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 4 )
location_assignment_dense_iron_treasure_2 =          DomeKeeperLocationData("Dense iron  - Treasure 2",         TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 5 )
location_assignment_barren_lands_treasure_2 =        DomeKeeperLocationData("Barren lands - Treasure 2",        TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 6 )
location_assignment_defective_weapon_treasure_2 =    DomeKeeperLocationData("Defective weapon - Treasure 2",    TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 7 )
location_assignment_heavy_hitters_treasure_2 =       DomeKeeperLocationData("Heavy hitters - Treasure 2",       TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 8 )
location_assignment_swiss_cheese_treasure_2 =        DomeKeeperLocationData("Swiss cheese - Treasure 2",        TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 9 )
location_assignment_logistical_problem_treasure_2 =  DomeKeeperLocationData("Logistical problem - Treasure 2",  TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 10)
location_assignment_high_risk_treasure_2 =           DomeKeeperLocationData("High risk - Treasure 2",           TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 11)
location_assignment_monster_masses_treasure_2 =      DomeKeeperLocationData("Monster masses - Treasure 2",      TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 12)
location_assignment_iron_shortage_treasure_2 =       DomeKeeperLocationData("Iron shortage - Treasure 2",       TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 13)
location_assignment_mining_problem_treasure_2 =      DomeKeeperLocationData("Mining problem - Treasure 2",      TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 14)
location_assignment_cobalt_contribution_treasure_2 = DomeKeeperLocationData("Cobalt contribution - Treasure 2", TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 15)
location_assignment_broken_comms_treasure_2 =            DomeKeeperLocationData("Broken comms - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 16)
location_assignment_darkness_treasure_2 =                DomeKeeperLocationData("Darkness - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 17)
location_assignment_tree_farm_treasure_2 =               DomeKeeperLocationData("Tree farm - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 18)
location_assignment_acid_rain_treasure_2 =               DomeKeeperLocationData("Acid rain - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 19)
location_assignment_hazardous_iron_treasure_2 =          DomeKeeperLocationData("Hazardous - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 20)
location_assignment_emergency_treasure_2 =               DomeKeeperLocationData("Emergency - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 21)
location_assignment_brutal_monsters_treasure_2 =         DomeKeeperLocationData("Brutal monsters - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 22)
location_assignment_logistical_nightmare_treasure_2 =    DomeKeeperLocationData("Logistical - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 23)
location_assignment_survival_of_the_fittest_treasure_2 = DomeKeeperLocationData("Survival of the fittest - Treasure 2",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 1 + 24)


#location_assignment_showdown_treasure_3 =            DomeKeeperLocationData("Showdown regular - Treasure 3",    TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 0 )
#location_assignment_iron_contribution_treasure_3 =   DomeKeeperLocationData("Iron contribution - Treasure 3",   TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 1 )
#location_assignment_upside_down_treasure_3 =         DomeKeeperLocationData("Upside down - Treasure 3",         TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 2 )
#location_assignment_maze_treasure_3 =                DomeKeeperLocationData("Maze regular - Treasure 3",        TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 3 )
#location_assignment_projectile_hell_treasure_3 =     DomeKeeperLocationData("Projectile hell - Treasure 3",     TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 4 )
#location_assignment_dense_iron_treasure_3 =          DomeKeeperLocationData("Dense iron  - Treasure 3",         TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 5 )
#location_assignment_barren_lands_treasure_3 =        DomeKeeperLocationData("Barren lands - Treasure 3",        TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 6 )
#location_assignment_defective_weapon_treasure_3 =    DomeKeeperLocationData("Defective weapon - Treasure 3",    TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 7 )
#location_assignment_heavy_hitters_treasure_3 =       DomeKeeperLocationData("Heavy hitters - Treasure 3",       TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 8 )
#location_assignment_swiss_cheese_treasure_3 =        DomeKeeperLocationData("Swiss cheese - Treasure 3",        TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 9 )
#location_assignment_logistical_problem_treasure_3 =  DomeKeeperLocationData("Logistical problem - Treasure 3",  TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 10)
#location_assignment_high_risk_treasure_3 =           DomeKeeperLocationData("High risk - Treasure 3",           TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 11)
#location_assignment_monster_masses_treasure_3 =      DomeKeeperLocationData("Monster masses - Treasure 3",      TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 12)
#location_assignment_iron_shortage_treasure_3 =       DomeKeeperLocationData("Iron shortage - Treasure 3",       TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 13)
#location_assignment_mining_problem_treasure_3 =      DomeKeeperLocationData("Mining problem - Treasure 3",      TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 14)
#location_assignment_cobalt_contribution_treasure_3 = DomeKeeperLocationData("Cobalt contribution - Treasure 3", TREASURE_ASYNC_FIRST_ID + ASSIGNMENTS_AMOUNT * 2 + 15)

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
    location_assignment_completion_regular_cobalt_contribution,
    location_assignment_completion_regular_broken_comms,
    location_assignment_completion_regular_darkness,
    location_assignment_completion_regular_tree_farm,
    location_assignment_completion_regular_acid_rain,
    location_assignment_completion_regular_hazardous_iron,
    location_assignment_completion_regular_emergency,
    location_assignment_completion_regular_brutal_monsters,
    location_assignment_completion_regular_logistical_nightmare,
    location_assignment_completion_regular_survival_of_the_fittest
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
    location_assignment_completion_challenge_cobalt_contribution,
    location_assignment_completion_challenge_broken_comms,
    location_assignment_completion_challenge_darkness,
    location_assignment_completion_challenge_tree_farm,
    location_assignment_completion_challenge_acid_rain,
    location_assignment_completion_challenge_hazardous_iron,
    location_assignment_completion_challenge_emergency,
    location_assignment_completion_challenge_brutal_monsters,
    location_assignment_completion_challenge_logistical_nightmare,
    location_assignment_completion_challenge_survival_of_the_fittest
]

location_assignments_first_treasure : list[DomeKeeperLocationData] = [
    location_assignment_showdown_treasure_1,     
    location_assignment_iron_contribution_treasure_1,
    location_assignment_upside_down_treasure_1,     
    location_assignment_maze_treasure_1,          
    location_assignment_projectile_hell_treasure_1,
    location_assignment_dense_iron_treasure_1,    
    location_assignment_barren_lands_treasure_1,  
    location_assignment_defective_weapon_treasure_1,
    location_assignment_heavy_hitters_treasure_1,  
    location_assignment_swiss_cheese_treasure_1,   
    location_assignment_logistical_problem_treasure_1,
    location_assignment_high_risk_treasure_1,        
    location_assignment_monster_masses_treasure_1,  
    location_assignment_iron_shortage_treasure_1,   
    location_assignment_mining_problem_treasure_1,  
    location_assignment_cobalt_contribution_treasure_1,
    location_assignment_broken_comms_treasure_1,
    location_assignment_darkness_treasure_1,
    location_assignment_tree_farm_treasure_1,
    location_assignment_acid_rain_treasure_1,
    location_assignment_hazardous_iron_treasure_1,
    location_assignment_emergency_treasure_1,
    location_assignment_brutal_monsters_treasure_1,
    location_assignment_logistical_nightmare_treasure_1,
    location_assignment_survival_of_the_fittest_treasure_1
]

location_assignments_second_treasure : list[DomeKeeperLocationData] = [
    location_assignment_showdown_treasure_2,     
    location_assignment_iron_contribution_treasure_2,
    location_assignment_upside_down_treasure_2,     
    location_assignment_maze_treasure_2,          
    location_assignment_projectile_hell_treasure_2,
    location_assignment_dense_iron_treasure_2,    
    location_assignment_barren_lands_treasure_2,  
    location_assignment_defective_weapon_treasure_2,
    location_assignment_heavy_hitters_treasure_2,  
    location_assignment_swiss_cheese_treasure_2,   
    location_assignment_logistical_problem_treasure_2,
    location_assignment_high_risk_treasure_2,        
    location_assignment_monster_masses_treasure_2,  
    location_assignment_iron_shortage_treasure_2,   
    location_assignment_mining_problem_treasure_2,  
    location_assignment_cobalt_contribution_treasure_2,
    location_assignment_broken_comms_treasure_2,
    location_assignment_darkness_treasure_2,
    location_assignment_tree_farm_treasure_2,
    location_assignment_acid_rain_treasure_2,
    location_assignment_hazardous_iron_treasure_2,
    location_assignment_emergency_treasure_2,
    location_assignment_brutal_monsters_treasure_2,
    location_assignment_logistical_nightmare_treasure_2,
    location_assignment_survival_of_the_fittest_treasure_2
]

#location_assignments_third_treasure : list[DomeKeeperLocationData] = [
#    location_assignment_showdown_treasure_3,
#    location_assignment_iron_contribution_treasure_3,
#    location_assignment_upside_down_treasure_3,
#    location_assignment_maze_treasure_3,
#    location_assignment_projectile_hell_treasure_3,
#    location_assignment_dense_iron_treasure_3,
#    location_assignment_barren_lands_treasure_3,
#    location_assignment_defective_weapon_treasure_3,
#    location_assignment_heavy_hitters_treasure_3,
#    location_assignment_swiss_cheese_treasure_3,
#    location_assignment_logistical_problem_treasure_3,
#    location_assignment_high_risk_treasure_3,
#    location_assignment_monster_masses_treasure_3,
#    location_assignment_iron_shortage_treasure_3,
#    location_assignment_mining_problem_treasure_3,
#    location_assignment_cobalt_contribution_treasure_3
#]
#endregion

def generate_locations_data() -> list[DomeKeeperLocationData] :
    rtr: list[DomeKeeperLocationData] = []
    rtr.extend(location_table_easy_upgrades.copy())
    rtr.extend(location_table_normal_upgrades.copy())
    rtr.extend(location_table_hard_upgrades.copy())
    rtr.extend(location_assignments_regular.copy())
    rtr.extend(location_assignments_challenge.copy())
    rtr.extend(location_assignments_first_treasure.copy())
    rtr.extend(location_assignments_second_treasure.copy())
    #rtr.extend(location_assignments_third_treasure.copy())
    rtr.extend(generate_switches_locations())
    rtr.extend(generate_caves_locations())
    rtr.extend(generate_treasures_locations())
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

def generate_treasures_locations() -> list[DomeKeeperLocationData] :
    rtr = []
    for i in range(LAYERS_MAX_AMOUNT):
        rtr.append(DomeKeeperLocationData("Layer " + str(i + 1) + " - Treasure", TREASURE_SYNC_FIRST_ID + i))
    return rtr

def get_non_switch_location_count(layers: int) -> int:
    """Count locations that are never switch-locations for Relic Hunt modes."""

    upgrades_count = (
        len(location_table_easy_upgrades)
        + len(location_table_normal_upgrades)
        + len(location_table_hard_upgrades)
    )
    caves_count = layers
    treasures_count = layers

    return upgrades_count + caves_count + treasures_count