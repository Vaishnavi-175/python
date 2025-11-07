import array as arr

# Create an array of integers
numbers = arr.array('i', [10, 20, 30, 40, 50])

# 1. Display the array
print("Original array:", numbers)

# 2. Append an element
numbers.append(60)
print("After append:", numbers)

# 3. Insert an element at index 2
numbers.insert(2, 25)
print("After insert at index 2:", numbers)

# 4. Remove an element
numbers.remove(40)
print("After removing 40:", numbers)

# 5. Pop an element (remove last element)
popped = numbers.pop()
print("After pop:", numbers)
print("Popped element:", popped)

# Bonus: Access element by index
print("Element at index 3:", numbers[3])
