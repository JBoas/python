
lowernumber = input("")
highernumber = input("")
lowernumber = int(lowernumber)
highernumber = int(highernumber)


def palindrome(lowernumber, highernumber):
	palindromelist = []
	for number in range(lowernumber, highernumber + 1):
		x = 1
		number = str(number)
		while x <(len(number)):
			test = number[len(number) - x]
			print(test, number[x])
			x += 1          
			if test[0] == number[0]:
				palindromelist.append(number)
				print(palindromelist)
	return test
		
	
palindrome(lowernumber, highernumber)
	
	
	
'''
	msg = input("Enter")
	begin = 0
	end = -1
	
	
	
	
	
	
	
	
	
	
	while x < (len(msg)+1):
		fmsg = msg[len(msg) - x]
		x += 1
		print(fmsg)
		'''