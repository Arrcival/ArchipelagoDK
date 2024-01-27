import string
from BaseClasses import Item, ItemClassification, Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import ItemDataCode, item_table, item_engineer, item_assessor, item_laser, item_sword, item_artillery, item_tesla, item_gadget, item_cobalt
from .Options import Dome, DomeKeeperOptions, Keeper
from .Locations import location_table
from .Regions import create_regions


class DomeKeeperItem(Item):
    game = "Dome Keeper"

    def __init__(self, code, name, player: int = None):
        super(DomeKeeperItem, self).__init__(
            name,
            ItemClassification.useful,
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
    item_name_to_id = {data.name: id for id, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}
    topology_present = True
    web = DomeKeeperWeb()
    required_client_version = (0, 4, 4)

    base_id = 4242001

    def set_rules(self):
        pass

    def create_items(self):
        # Fill out our pool with our items from item_pool, assuming 1 item if not present in item_pool
        pool = []
        print(self.options.keeper)
        print(self.options.keeper.value)
        if self.options.keeper == Keeper.option_Engineer:
            pool += generate_items(item_engineer, self.player)
        if self.options.keeper.value == Keeper.option_Assessor:
            pool += generate_items(item_assessor, self.player)

        if self.options.dome == Dome.option_Laser:
            pool += generate_items(item_laser, self.player)
        if self.options.dome == Dome.option_Sword:
            pool += generate_items(item_sword, self.player)
        if self.options.dome == Dome.option_Artillery:
            pool += generate_items(item_artillery, self.player)
        if self.options.dome == Dome.option_Tesla:
            pool += generate_items(item_tesla, self.player)
        
        # Always has a primary gadget
        pool += generate_items(item_gadget, self.player)

        pool += generate_junk_cobalts(self.player, len(location_table) - len(pool))

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
        }

def generate_items(itemDataCode: ItemDataCode, player):
    values = []
    for _ in range(itemDataCode.data.count):
        values.append(DomeKeeperItem(itemDataCode.code, itemDataCode.data.name, player))
    return values

def generate_junk_cobalts(player, amount):
    values = []
    for _ in range(amount):
        values.append(DomeKeeperItem(item_cobalt.code, item_cobalt.data.name, player))
    return values
