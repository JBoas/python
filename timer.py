import time

hour = input("Enter hours ")
hour = int(hour)
for h1 in range(hour):
	for m1 in range(6):
		for m2 in range(10):
			for s2 in range(6):
				for s3 in range(10):
					print(h1,":",m1,m2,":",s2,s3)
					time.sleep(0.1)
