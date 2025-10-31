li = []
n = int(input("Enter the element in list: "))

for i in range(0,n):
	li.append(input("Enter thr item: "))

print("printing the item in list:", end = " ")

for i in li:
	print(i, end = " ")
