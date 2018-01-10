palindromes = []

for number in range(100,10000):
	strnumber = str(number)
	
	if len(strnumber) == 3:
		if strnumber[0] == strnumber[2]:
			if (int(strnumber[0])%2) == 0 and (int(strnumber[1])%2) == 0 and (int(strnumber[2])%2) == 0:
				palindromes.append(strnumber)
	
	elif len(strnumber) == 4:
		if strnumber[0] == strnumber[3]:
			if (int(strnumber[0])%2) == 0 and (int(strnumber[1])%2) == 0 and (int(strnumber[2])%2) == 0 and (int(strnumber[3])%2) == 0 and int(strnumber[1]) == int(strnumber[2]):
				palindromes.append(strnumber)
	
	
print(palindromes)