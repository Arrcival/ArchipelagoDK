import string
from BaseClasses import Item, ItemClassification, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import (
    ItemDataCode,
    generate_all_items,
    items_engineer,
    items_assessor,
    items_laser,
    items_sword,
    items_artillery,
    items_tesla,
    items_shield,
    items_orchard,
    items_repellent,
    item_trap_wavestart,
    item_filler_cobalt
)
from .Options import Dome, DomeKeeperOptions, Keeper, DomeGadget
from .Locations import generate_locations, get_locations_amount, SWITCHES_AMOUNT
from .Regions import create_regions


class DomeKeeperItem(Item):
    game = "Dome Keeper"

    def __init__(self, code, name, classification, player: int = None):
        super(DomeKeeperItem, self).__init__(
            name,
            classification,
            code,
            player
        )


class DomeKeeperWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Dome Keeper for Archipelago. "
        "",
        "English",
        "dome_keeper_en.md",
        "dome_keeper/en",
        ["Arrcival"]
    )]

class DomeKeeperWorld(World):
    """Dome Keeper is a roguelike/mining game where you need to dig up a relic while defending waves of enemies."""

    game = "Dome Keeper"  # name of the game/world
    options_dataclass = DomeKeeperOptions
    options: DomeKeeperOptions
    item_name_to_id = {data.name: id for id, data in generate_all_items().items()}
    location_name_to_id = {name: data.code for name, data in generate_locations().items()}
    topology_present = True
    web = DomeKeeperWeb()
    required_client_version = (0, 4, 4)

    base_id = 4242001

    def set_rules(self):
        pass

    def create_items(self):
        # Fill out our pool with our items from item_pool, assuming 1 item if not present in item_pool
        pool: list[Item] = []
        if self.options.keeper == Keeper.option_Engineer:
            pool += generate_items(items_engineer, self.player)
        if self.options.keeper == Keeper.option_Assessor:
            pool += generate_items(items_assessor, self.player)

        if self.options.dome == Dome.option_Laser:
            pool += generate_items(items_laser, self.player)
        if self.options.dome == Dome.option_Sword:
            pool += generate_items(items_sword, self.player)
        if self.options.dome == Dome.option_Artillery:
            pool += generate_items(items_artillery, self.player)
        if self.options.dome == Dome.option_Tesla:
            pool += generate_items(items_tesla, self.player)
        
        if self.options.dome_gadget == DomeGadget.option_Orchard:
            pool += generate_items(items_orchard, self.player)
        if self.options.dome_gadget == DomeGadget.option_Repellent:
            pool += generate_items(items_repellent, self.player)
        if self.options.dome_gadget == DomeGadget.option_Shield:
            pool += generate_items(items_shield, self.player)

        pool += generate_junk_cobalts(self.player, get_locations_amount() - len(pool))

        self.multiworld.itempool += pool

    def create_item(self, name: str) -> Item:
        return DomeKeeperItem(name, self.player)
    
    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def fill_slot_data(self) -> dict:
        return {
            "seed": "".join(self.multiworld.per_slot_randoms[self.player].choice(string.digits) for _ in range(8)),
            "keeper": self.options.keeper.value,
            "dome": self.options.dome.value,
            "domeGadget": self.options.dome_gadget.value,
            "mapSize": self.options.map_size.value,
            "difficulty": self.options.difficulty.value,
            "deathLink": self.options.death_link.value,
            "switchesAmount": SWITCHES_AMOUNT
        }

def generate_items(itemDataCodes: list[ItemDataCode], player):
    values = []
    for itemDataCode in itemDataCodes:
        #print("Item data count of " + itemDataCode.data.name + " : " + str(itemDataCode.data.count))
        for _ in range(itemDataCode.data.count):
            values.append(DomeKeeperItem(itemDataCode.code, itemDataCode.data.name, itemDataCode.data.classification, player))
    return values

def generate_junk_cobalts(player, amount):
    # edit later for traps
    values = []
    for _ in range(amount):
        values.append(DomeKeeperItem(item_filler_cobalt.code, item_filler_cobalt.data.name, item_filler_cobalt.data.classification, player))
    return values
