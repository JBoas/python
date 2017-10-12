sunny = input("is it sunny? y/n")
hour = input("what is the hour of day?")
hour = int(hour)

isSunnyOutside = sunny == "y"
isBetween4and8 = hour >= 4 and hour <= 8

if(isSunnyOutside and isBetween4and8):
	print("The squirrels are playing outside")
else:
	print("the squirrels are sleeping")
