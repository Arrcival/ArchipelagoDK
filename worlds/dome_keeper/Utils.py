LAYER_PREFIX = "Layer"
ENTRANCE_SUFFIX = " entrance"

GUILD_ASSIGNMENT_NAMES = [
    "Showdown",
    "Iron contribution",
    "Upside down",
    "Maze",
    "Projectile hell",
    "Dense iron",
    "Barren lands",
    "Defective weapon",
    "Heavy hitters",
    "Swiss cheese",
    "Logistical problem",
    "High risk",
    "Monster masses ",
    "Iron shortage",
    "Mining problem",
    "Cobalt contribution",
]

GUILD_ASSIGNMENT_NAMES_WITH_DLC = GUILD_ASSIGNMENT_NAMES + [
    "Broken comms",
    "Darkness",
    "Tree Farm",
    "Acid Rain",
    "Hazardous Iron",
    "Emergency",
    "Brutal Monsters",
    "Logistical Nightmare",
    "Survival of the Fittest",
]

ASSIGNMENTS_AMOUNT: int = len(GUILD_ASSIGNMENT_NAMES)
ASSIGNMENTS_AMOUNT_WITH_DLC: int = len(GUILD_ASSIGNMENT_NAMES_WITH_DLC)


def layer_region_name(layer_number: int) -> str:
    return f"{LAYER_PREFIX} {layer_number}"

def layer_entrance_name(from_layer_number: int) -> str:
    # entrance from layer N to layer N+1
    return f"{layer_region_name(from_layer_number)}{ENTRANCE_SUFFIX}"

def assignment_entrance_name(assignment_id: int) -> str:
    return GUILD_ASSIGNMENT_NAMES_WITH_DLC[assignment_id]