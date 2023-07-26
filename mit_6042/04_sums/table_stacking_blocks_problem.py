

def spread(n):

	# not recursive, left edge
	left_most_edge = 1 - 1/(2*n)
	
	# Base cases
	if n == 1:
		right_most_edge = 1/2
		return max(left_most_edge, right_most_edge)
		
	# Constructor case
	return max(left_most_edge, spread(n-1) + 1/(2*n))

if __name__ == '__main__':
	
	n = 3
	Sn = spread(n)
	print(Sn)
