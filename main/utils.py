from typing import List
from main.models import Inventory


# func to prepare dict of items and calculate its quantity
def items_calc(items: List[Inventory]) -> dict:
    inventories = {}
    for item in items:
        if item.name not in inventories:
            inventories[item.name.__str__()] = {"name": item.name.__str__(), "count": 1}
        else:
            inventories[item.name.__str__()]["count"] += 1
    return inventories






