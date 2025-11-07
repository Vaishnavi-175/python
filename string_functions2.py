# Create a string
text = "  Hello, Python World!  "

print("Uppercase:", text.upper())


print("Lowercase:", text.lower())


print("Stripped:", text.strip())


print("Replace 'Python' with 'Programming':", text.replace("Python", "Programming"))


words = text.strip().split()
print("Split into words:", words)

position = text.find("Python")
print("Position of 'Python':", position)
