
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

print("Name:", student.get("name"))


student["grade"] = "A"
print("After adding grade:", student)

student["age"] = 21
print("After updating age:", student)

removed_value = student.pop("course")
print("After removing course:", student)
print("Removed value:", removed_value)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
