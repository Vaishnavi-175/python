l = [10, 20 , 30 ,40, 50, 60]
print("Type of object is: ", type(l))

l.append(70)
print("70 is appended: ", l)

l.insert(90, 2)
print("90 is inserted: ", l)

l1 = [100, 300, 400, 900]
l.extend(l1)
print("Extended List is: ", l)

l.sort()
print("Sorted list is: ", l)

l.reverse()
print("Reverse list is: ", l)

l2 = l.copy()
print("Copied list is: ", l2)

l.pop()
print("Last element is Poped: ", l)

l.remove(900)
print("900 is remove: ", l)

l.append(900)
l.append(900)

print("900 Occurance is: ", l.count(900))