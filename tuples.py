# 1.STUDENT REGISTRATION
student = ("Dara", 20, "Computer Science", "Year 3")

print("Student Name:", student[0])
print("Student Major:", student[2])
print("Total number of items:", len(student))
print("Student Year:", student[-1])

# 2. COURSE ENROLLMENT
courses = ("Python", "Databse", "Networking", "Python", "Web Development")
print("Total Python courses:", courses.count("Python"))
print("The index of 'Networking' course is:", courses.index("Networking"))
for course in courses:
    print(course)

# 3. UPDATING STUDENT COURSE
registered_courses = ("Python", "Database", "Networking")
registered_list = list(registered_courses)
registered_list.append("Cloud Computing")
registered_courses = tuple(registered_list)
print("Updated Registered Courses:", registered_courses)