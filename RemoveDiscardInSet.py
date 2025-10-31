Months = set(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"))

print(Months)

Months.discard("Jan")
Months.discard("Apr")

print("Months after Discard: ", end = " ")
print(Months)


Months.remove("Feb")
Months.remove("Mar")
print(Months)
