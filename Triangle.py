n = 5
for i in range(0, n):
	ch = 65
	for j in range(0, i+1):
		print(chr(ch), end = " ")
		ch += 1
	print()