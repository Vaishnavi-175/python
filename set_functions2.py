# Create a set
numbers = {10, 20, 30, 40, 50}


numbers.add(60)
print("After add:", numbers)


numbers.remove(20)
print("After remove:", numbers)


numbers.discard(100)
print("After discard:", numbers)


popped = numbers.pop()
print("After pop:", numbers)
print("Popped element:", popped)

numbers.clear()
print("After clear:", numbers)
