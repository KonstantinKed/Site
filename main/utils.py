from typing import List
from main.models import Inventory


# func to prepare list of items and calculate it's quantity
def items_calc(items: List[Inventory]) -> dict:
    inventories = {}
    for item in items:
        if item.name not in inventories:
            inventories[item.name] = {"name": item.name, "count": 1}
        else:
            inventories[item.name]["count"] += 1
    return inventories






