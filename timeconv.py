seconds = input("Enter Time in Seconds")

hour = int(seconds)/3600
calcminute = int(seconds)%3600
finalhour = int(hour)

minute = (calcminute)/60
second = (calcminute)%60
finalminute = int(minute)

print(finalhour, "hours", finalminute, "minutes", second, "seconds")

