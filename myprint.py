def my_print(msg):
	okblue = '\033[94m'
	okgreen = '\033[92m'
	warning = '\033[93m'
	fail = '\033[91m'
	endc = '\033[0m'
	print(okgreen + msg + endc)

my_print("sentence")
