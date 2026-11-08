# PRACTICE SHEET: DICTIONARY

# 1. Create a dictionary called inventory with 3 products and their stock numbers.
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 20,
}
print("1. Initial Inventory:", inventory)


# 2. Use get() to check the stock of a product that may not exist.
dragonfruit_stock = inventory.get("dragonfruit", 0)
print("2. Dragonfruit stock:", dragonfruit_stock)


# 3. Use update() to add 2 new products and change one stock number.
inventory.update({
    "apples": 65,
    "mangoes": 40,
    "grapes": 25,
})
print("3. Inventory after update:", inventory)


# 4. Use items() to print every product and its stock.
print("4. Product listings:")
for product, stock in inventory.items():
    print(f"   - {product}: {stock}")


# 5. Use pop() to remove a product that is sold out.
removed_stock = inventory.pop("bananas")
print(f"5. Removed 'bananas' (previously {removed_stock} in stock):", inventory)


# 6. Use setdefault() to add a new product only if it is not already there.
inventory.setdefault("peaches", 15)
inventory.setdefault("apples", 100)
print("6. Inventory after setdefault:", inventory)


# 7. Use values() and sum() to print the total number of items in stock.
total_stock = sum(inventory.values())
print("7. Total items in stock:", total_stock)


# 8. Use copy() to save a backup, then clear() the original.
backup_inventory = inventory.copy()
inventory.clear()

print("8. Original inventory (cleared):", inventory)
print("   Backup inventory:", backup_inventory)