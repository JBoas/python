def add(x,y):
	s=x+y
	return(s)


def multiply(a,b):
	total = 0
	for x in range(b):
		total = add(total,b)
	return total

def power(j,b):
	total = 1
	for x in range(b):
		total = multiply(j,b)
	return total
print(power(2,8))

