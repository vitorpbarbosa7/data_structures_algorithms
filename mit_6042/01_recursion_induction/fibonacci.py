
def fib(n):
	
	# Base cases
	if n == 0:
		return 0

	if n == 1:
		return 1

	# Constructor cases
	return fib(n-1) + fib(n-2)

for i in range(8):
	print(fib(i))
