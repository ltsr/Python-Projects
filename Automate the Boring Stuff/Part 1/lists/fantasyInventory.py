def displayInventory(inv):
    print("Inventory:")
    itemTotal = 0

    for k, v in inv.items():
        print(f"{v} {k}")
        itemTotal += v

    print(f"Total number of items: {itemTotal}")

stuff = { "rope" : 1, "torch" : 6, "gold coin" : 42, "dagger" : 1, "arrow" : 12}

displayInventory(stuff)