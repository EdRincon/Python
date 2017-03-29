# Inventory.py
stuff = {'rope' : 1, 'torch' : 6, 'gol coin' : 42, 'dagger' : 1, 'arrow' : 12}

def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0
    for k,v in inventory.items():
        # My code
        itemTotal = itemTotal + v
        print( str(v) + ' ' + k)
    print("Total number of items: " +str(itemTotal))

displayInventory(stuff)
