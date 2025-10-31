Months = set(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"))

print(Months)

Months.add("Dec")
Months.add("Aug")

print("Months after modify")
print(Months)

print("Looping through month: ")
for i in Months:
	print(i)

Months.update(["Jul", "Aug", "Sep", "Oct"])
print(Months)
