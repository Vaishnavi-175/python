num = int(input("Enter Number: "))
rev = 0
dig = 1
while(num != 0):
	dig = num % 10
	rev = rev * 10 + dig
	num //= 10
print(rev)