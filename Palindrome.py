num = int(input("Enter Number: "))
rev = 0
n = num
while(num != 0):
	dig = num % 10
	rev = rev * 10 + dig
	num //= 10
if n == rev:
	print("Given number is palindrome")
else:
	print("Given number is not palindrome")