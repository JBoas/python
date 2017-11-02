
import random

number = input("Enter Number:")
number = int(number)

answer = random.randint(0,25)

while(number > answer):
	print("Too High")
	number = input("enter a number:")
	number = int(number)
	if(number > answer):
		print("Too High")
	elif(number < answer):
		print("Too Low")
	else:
		print("You got it")
	if(number < answer):
		print("Too low")
		number = input("Enter a number")
		number = int(number)
		if(number > answer):
			print("Too High")
		elif(number < answer):
			print("Too low")
		else:
			print("That's it")
	else:
		print("That's it")

print(answer)
