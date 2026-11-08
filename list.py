# 1
shopping_list = ["apples", "milk", "bananas", "milk", "coffee"]

# 2
print("Second item:", shopping_list[1])
print("Last item:", shopping_list[-1])
print("Total items:", len(shopping_list))

# 3
shopping_list.append("eggs")
shopping_list.insert(1, "bread")

# 4
shopping_list.remove("milk")
print("Updated list after removing 'milk' once:", shopping_list)

# 5
print("Does 'milk' still exist?", "milk" in shopping_list)
print("Number of items remaining:", len(shopping_list))

# 6
print("\nItems in list:")
for item in shopping_list:
    print(item)
print("Total number of items:", len(shopping_list))

# 8
removed_item = shopping_list.pop()
print("\nRemoved item:", removed_item)
print("Updated list:", shopping_list)

# 9
unsorted_copy = shopping_list.copy()
sorted_list = sorted(shopping_list)

print("\nUnsorted copy:", unsorted_copy)
print("Sorted list:", sorted_list)