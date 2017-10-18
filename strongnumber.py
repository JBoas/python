strnumber = input("Enter number")
sum = 0
for strdigit in strnumber:
	digit = int(strdigit)
	x = 1
	for multiplyme in range(1,digit + 1):
		x = x * multiplyme
	print(strdigit + str(x))
	sum = sum + x
if int(strnumber) == (sum):
	print("Strong Number")
else:
	print("Nope")
