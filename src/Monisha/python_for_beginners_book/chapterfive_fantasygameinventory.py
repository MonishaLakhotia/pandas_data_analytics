#Display user inventory
def display_inventory(inventory):
  print('Inventory:')
  item_total = 0
  for k, v in inventory.items():
    print(v, k)
    item_total = item_total + inventory[k]
  print('Total number of items: ' + str(item_total))

#To add loot in user inventory
def add_to_inventory(inventory, add_items):
  #to turn loot into dictionary
  loot = {} 
  for items in add_items:
    loot.setdefault(items, 0)
    loot[items] = loot[items] + 1
  #to merge loot inventory to user inventory
  for items in loot:
    if items in inventory:
      inventory[items] = inventory[items] + loot[items]
    elif items not in inventory:
      inventory.setdefault(items, loot[items])

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 
'dagger': 1, 'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 
'gold coin', 'gold coin', 'ruby', 'ruby']

add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)