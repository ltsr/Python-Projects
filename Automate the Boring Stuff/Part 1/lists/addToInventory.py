def addToInventory(inventory:dict, addedItems:list):
    for add in addedItems:
        if str(add) in inventory.keys():
            inventory[str(add)] += 1
        else:
            inventory.update({str(add): 1})
            #inventory.setdefault(str(add), 1))

def displayInventory(inv:dict):
    print("Inventory:")
    itemTotal = 0

    for k, v in inv.items():
        print(f"{v} {k}")
        itemTotal += v

    print(f"Total number of items: {itemTotal}")
        
        
inv = {"gold coin" : 42, "rope" : 1}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]

addToInventory(inv, dragonLoot)
displayInventory(inv)