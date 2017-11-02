'''
-find how many digits are in a given number
-find a digit
--raise number to the power
-Find some of the powered digits
-Compare final number to input number
'''

def is_armstrong(number):
	print(number)
	strnumber = str(number)
	numberofdigits = len(strnumber)
	sum = 0

	for strdigit in strnumber:
		digit = int(strdigit)
		sum = sum + (digit**numberofdigits)
	if(sum == (int(strnumber))):
		return True
	else:
		return False
def generate_armstrong_numbers(highend):
	for x in range(highend):
		armstrong = is_armstrong(x)
		if(armstrong == True):
			print(str(x) + " Armstrong number. ")


generate_armstrong_numbers(1000000000000000)
