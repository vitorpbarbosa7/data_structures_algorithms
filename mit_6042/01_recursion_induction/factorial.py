
def fac(n):

	# correctness
	# invariant to be respected
	assert n >= 0
	
	assert isinstance(n,int)
	
	# Base case
	if n == 0:
		return 1	

	n = n - 1
	
	# Constructor (Recursive case)
	return (n+1)*fac(n)

print(fac(0))
print(fac(1))
print(fac(5))
print(fac(4))
#print(fac(-1))
print(fac(1.1))
	
