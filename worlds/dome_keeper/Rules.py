from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Item
from worlds.dome_keeper.Items import generate_unlocks
from worlds.dome_keeper.Regions import GUILD_ASSIGNMENT_NAMES
from worlds.generic.Rules import set_rule
from worlds.dome_keeper.Options import ProgressionType

if TYPE_CHECKING:
    from . import DomeKeeperWorld

def set_every_rules(world: "DomeKeeperWorld", player: int):
    if world.options.progression_type.value == ProgressionType.option_Guild_Assignments:
        set_guild_assignment_rules(world, player)
    elif world.options.progression_type.value == ProgressionType.option_Relic_Hunt_Progression_Layers:
        set_rh_progression_rules(world, player)
    else:
        set_rh_noprogression_rules(world, player)

def set_guild_assignment_rules(world: "DomeKeeperWorld", player: int):
    unlocks = get_unlocks_without_starting(player, world.options.first_assignment.value)
    guild_assignments_names = GUILD_ASSIGNMENT_NAMES.copy()
    guild_assignments_names.pop(world.options.first_assignment.value)
    for i in range(len(guild_assignments_names)):
        set_rule(world.multiworld.get_entrance("Menu -> " + guild_assignments_names[i], player),
            lambda state: state.has(unlocks[i].name, player))

def set_rh_progression_rules(world: "DomeKeeperWorld", player: int):
    set_rule(world.multiworld.get_entrance("Layer 1 -> Layer 2", player),
                lambda state: state.has("Layer unlock", player, 1) and has_mining_upgrade(state, player, 2))
    set_rule(world.multiworld.get_entrance("Layer 2 -> Layer 3", player),
                lambda state: state.has("Layer unlock", player, 2) and has_mining_upgrade(state, player, 3))
    if world.options.map_size.value >= 1:
        set_rule(world.multiworld.get_entrance("Layer 3 -> Layer 4", player),
                lambda state: state.has("Layer unlock", player, 3) and has_mining_upgrade(state, player, 4))
    if world.options.map_size.value >= 2:
        set_rule(world.multiworld.get_entrance("Layer 4 -> Layer 5", player),
                lambda state: state.has("Layer unlock", player, 4) and has_mining_upgrade(state, player, 5))
        set_rule(world.multiworld.get_entrance("Layer 5 -> Layer 6", player),
                lambda state: state.has("Layer unlock", player, 5))
    if world.options.map_size.value >= 3:
        set_rule(world.multiworld.get_entrance("Layer 6 -> Layer 7", player),
                lambda state: state.has("Layer unlock", player, 6))

def set_rh_noprogression_rules(world: "DomeKeeperWorld", player: int):
    set_rule(world.multiworld.get_entrance("Layer 1 -> Layer 2", player),
        lambda state: has_mining_upgrade(state, player, 2))
    set_rule(world.multiworld.get_entrance("Layer 2 -> Layer 3", player),
        lambda state: has_mining_upgrade(state, player, 3))
    if world.options.map_size.value >= 1:
        set_rule(world.multiworld.get_entrance("Layer 3 -> Layer 4", player),
            lambda state: has_mining_upgrade(state, player, 4))
    if world.options.map_size.value >= 2:
        set_rule(world.multiworld.get_entrance("Layer 4 -> Layer 5", player),
            lambda state: has_mining_upgrade(state, player, 5))
        
def has_mining_upgrade(state: CollectionState, player: int, tier: int) -> bool:
    return state.has("Drill upgrade", player, tier) or state.has("Kinetic spheres", player, tier)

def get_unlocks_without_starting(player: int, first_assignment: int) -> list[Item]:
    unlocks: list[Item] = generate_unlocks(player)
    unlocks.pop(first_assignment)
    return unlocks
