li = [0, 1, 2, 3, 10]
print("Print orignal list: ", end = " ")
for i in li:
	print(i, end = " ")

li.remove(2)

print(li)

li.remove(10)

print("List After Remove element: ", li)