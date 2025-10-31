x = int(input("Enter Limit: "))
sum = 0
i = 1

while(i <= x):
	if(i % 2 == 0):
		sum += i
	i += 1
print(sum)