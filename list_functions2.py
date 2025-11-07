# Create a list
numbers = [10, 20, 30, 40, 50]

# 1. Append an element
numbers.append(60)
print("After append:", numbers)

# 2. Insert an element at index 2
numbers.insert(2, 25)
print("After insert at index 2:", numbers)

# 3. Remove an element
numbers.remove(40)
print("After removing 40:", numbers)

# 4. Pop an element (remove last element)
popped = numbers.pop()
print("After pop:", numbers)
print("Popped element:", popped)

# 5. Reverse the list
numbers.reverse()
print("After reverse:", numbers)

# Bonus: Sort the list
numbers.sort()
print("After sort:", numbers)
