from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Item
from worlds.dome_keeper.Items import (
    generate_keys,
    generate_unlocks,
    item_assessor_spheres_strength,
    item_engineer_drill,
    item_infiltrator_progressive_mining,
    item_beastmaster_mining,
    item_layer_unlock,
    item_keys
)
from worlds.dome_keeper.Utils import layer_entrance_name, GUILD_ASSIGNMENT_NAMES, assignment_entrance_name
from worlds.generic.Rules import set_rule
from worlds.dome_keeper.Options import ProgressionType
from worlds.dome_keeper.Locations import generate_chests_locations

if TYPE_CHECKING:
    from . import DomeKeeperWorld

def set_every_rules(world: "DomeKeeperWorld", player: int):
    if world.options.progression_type.value == ProgressionType.option_Guild_Assignments:
        set_guild_assignment_rules(world, player)
    else:
        set_rh_progression_rules(world, player)

def set_guild_assignment_rules(world: "DomeKeeperWorld", player: int):
    first_assignment = world.options.first_assignment.value
    unlocks = get_unlocks_without_starting(player, first_assignment)

    assignment_indexes_to_lock = [
        i for i in range(len(GUILD_ASSIGNMENT_NAMES)) if i != first_assignment
    ]

    for unlock, assignment_index in zip(unlocks, assignment_indexes_to_lock):
        set_rule(
            world.multiworld.get_entrance(assignment_entrance_name(assignment_index), player),
            lambda state, unlock_name=unlock.name: state.has(unlock_name, player)
        )

def set_rh_progression_rules(world: "DomeKeeperWorld", player: int):
    layers_amount = world.get_layers_amount_from_options()
    for layer_number in range(2, layers_amount + 1):
        if layer_number <= 5:
            set_rule(
                world.multiworld.get_entrance(layer_entrance_name(layer_number), player),
                lambda state, layer_number=layer_number: (
                    state.has(item_layer_unlock.name, player, layer_number - 1)
                    and has_mining_upgrade(state, player, layer_number)
                )
            )
        else:
            set_rule(
                world.multiworld.get_entrance(layer_entrance_name(layer_number), player),
                lambda state, layer_number=layer_number: state.has(
                    item_layer_unlock.name, player, layer_number - 1
                )
            )

    layers_amount = len(world.switches_per_layer)
    chest_locations = generate_chests_locations()
    for i in range(layers_amount):
        key_name = item_keys[i].name
        chest_name = chest_locations[i].name
        set_rule(
            world.multiworld.get_location(chest_name, player),
            lambda state, key_name=key_name: state.has(key_name, player)
        )

def has_mining_upgrade(state: CollectionState, player: int, tier: int) -> bool:
    return (state.has(item_engineer_drill.name, player, tier) 
        or state.has(item_assessor_spheres_strength.name, player, tier)
        or state.has(item_infiltrator_progressive_mining.name, player, tier)
        or state.has(item_beastmaster_mining.name, player, tier))

def get_unlocks_without_starting(player: int, first_assignment: int) -> list[Item]:
    unlocks: list[Item] = generate_unlocks(player)
    unlocks.pop(first_assignment)
    return unlocks
