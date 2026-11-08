# TASK 1: SETUP
yesterday = {"a.txt", "b.txt", "c.txt"}
today = {"b.txt", "c.txt", "d.txt"}

# TASK 2: NEW AND DELETED FILES
new_files = today - yesterday           
deleted_files = yesterday - today       

print("New files:", new_files)
print("Deleted files:", deleted_files)

# TASK 3: UNCHANGED FILES
unchanged_files = yesterday.intersection(today)
print("\nUnchanged files:", unchanged_files)

# TASK 4: ALL CHANGES
all_changes = yesterday.symmetric_difference(today)
print("\nAll changed files:", all_changes)

# TASK 5: ALL FILES EVER SEEN
all_files = yesterday.union(today)
print("All files seen:", all_files)