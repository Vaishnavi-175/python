n = int(input("Enter Limit: "))
t1 = 0
t2 = 1
t3 = 1
print("Fibonacci Series: ")
print(t1, "," , t2, end = ", ")
while(t3 <= n):
	t3 = t1 + t2
	t1 = t2
	t2 = t3
	print(t3, end = ", ")
