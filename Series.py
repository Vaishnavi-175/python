def factorial(n):
	fact = 1
	for i in range(1, n+1):
		fact *= i
	return fact

sum = 1.0
n = 5 
for i in range(1, n):
	sum += 1 / factorial(i)

print(sum)