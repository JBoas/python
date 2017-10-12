
number = input("Enter A Number ")

length = len(number)
x = 0

totalsum = 0

while(x < length):
	addnumber = int(number[x])
	totalsum =  totalsum + addnumber
	x = x + 1
	print(totalsum)
