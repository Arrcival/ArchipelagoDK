from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from . import DomeKeeperWorld

def set_rules_colored_layers(world: "DomeKeeperWorld", player: int):
    if world.options.colored_layers.value:
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
        
    else:
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