from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Item
from worlds.dome_keeper.Items import (
    generate_unlocks,
    item_assessor_spheres_strength,
    item_engineer_drill,
    item_infiltrator_progressive_mining,
    item_beastmaster_catgoblin_amount,
    item_layer_unlock
)
from worlds.dome_keeper.Regions import GUILD_ASSIGNMENT_NAMES, layer_entrance_name
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
        unlock_name = unlocks[i].name
        set_rule(
            world.multiworld.get_entrance("Menu -> " + guild_assignments_names[i], player),
            lambda state, unlock_name=unlock_name: state.has(unlock_name, player)
        )

def set_rh_progression_rules(world: "DomeKeeperWorld", player: int):
    set_rule(world.multiworld.get_entrance(layer_entrance_name(2), player),
                lambda state: state.has(item_layer_unlock.name, player, 1) and has_mining_upgrade(state, player, 2))
    set_rule(world.multiworld.get_entrance(layer_entrance_name(3), player),
                lambda state: state.has(item_layer_unlock.name, player, 2) and has_mining_upgrade(state, player, 3))
    if world.options.map_size.value >= 1:
        set_rule(world.multiworld.get_entrance(layer_entrance_name(4), player),
                lambda state: state.has(item_layer_unlock.name, player, 3) and has_mining_upgrade(state, player, 4))
    if world.options.map_size.value >= 2:
        set_rule(world.multiworld.get_entrance(layer_entrance_name(5), player),
                lambda state: state.has(item_layer_unlock.name, player, 4) and has_mining_upgrade(state, player, 5))
        set_rule(world.multiworld.get_entrance(layer_entrance_name(6), player),
                lambda state: state.has(item_layer_unlock.name, player, 5))
    if world.options.map_size.value >= 3:
        set_rule(world.multiworld.get_entrance(layer_entrance_name(7), player),
                lambda state: state.has(item_layer_unlock.name, player, 6))

def set_rh_noprogression_rules(world: "DomeKeeperWorld", player: int):
    set_rule(world.multiworld.get_entrance(layer_entrance_name(2), player),
        lambda state: has_mining_upgrade(state, player, 2))
    set_rule(world.multiworld.get_entrance(layer_entrance_name(3), player),
        lambda state: has_mining_upgrade(state, player, 3))
    if world.options.map_size.value >= 1:
        set_rule(world.multiworld.get_entrance(layer_entrance_name(4), player),
            lambda state: has_mining_upgrade(state, player, 4))
    if world.options.map_size.value >= 2:
        set_rule(world.multiworld.get_entrance(layer_entrance_name(5), player),
            lambda state: has_mining_upgrade(state, player, 5))
        
def has_mining_upgrade(state: CollectionState, player: int, tier: int) -> bool:
    return (state.has(item_engineer_drill.name, player, tier) 
        or state.has(item_assessor_spheres_strength.name, player, tier)
        or state.has(item_infiltrator_progressive_mining.name, player, tier)
        or state.has(item_beastmaster_catgoblin_amount.name, player, tier))

def get_unlocks_without_starting(player: int, first_assignment: int) -> list[Item]:
    unlocks: list[Item] = generate_unlocks(player)
    unlocks.pop(first_assignment)
    return unlocks
