wordcount = {}

inputstring = "the dog ate a lot of food"
for word in inputstring.split(' '):
	if (word in wordcount):
		wordcount[word] = wordcount[word]+ 1
	else:
		wordcount[word] = 1

	
print(wordcount)