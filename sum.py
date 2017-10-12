adding = True
sum = 0
while(adding):
	num1 = input("Enter a Number ")
	num1 = float(num1)
	sum = sum +num1
	print(sum)
	print("Add again? y or n")
	add_again = input()
	adding = add_again == "y"
