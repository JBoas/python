temp = input("What is the temperature in celcius?")
temp = float(temp)

isfreezing = temp <= 0.0
isnormal = temp <= 100.0 and temp > 0.0
isgas = temp > 100.0

if(isfreezing):
	print("Ice")
elif(isnormal):
	print("Water")
elif(isgas):
	print("Air")

else:
	print("Unknown")
