#Tests to check the result of the polynomials.
#import package_name(moving_graphs)

def testpolynomialresult():
	coeffs=[i for i in range(0,15)]
	xs=[x for x in range(1,5)]
	#Results as computed from numpy polyval function. For accuracy these tests should be replaced with exponential rather then Horner's rule.
	results={1: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105], 
		2: [0, 1, 4, 11, 26, 57, 120, 247, 502, 1013, 2036, 4083, 8178, 16369, 32752], 
		3: [0, 1, 5, 18, 58, 179, 543, 1636, 4916, 14757, 44281, 132854, 398574, 1195735, 3587219], 
		4: [0, 1, 6, 27, 112, 453, 1818, 7279, 29124, 116505, 466030, 1864131, 7456536, 29826157, 119304642], 
		5: [0, 1, 7, 38, 194, 975, 4881, 24412, 122068, 610349, 3051755, 15258786, 76293942, 381469723, 1907348629]
	}
	passed=[]
	for x in xs:
		for ind in range(1,len(coeffs)+1):
			coeff=coeffs[0:ind]
			#call the function for polynomial
			#get the result
			#compare it with the above result
			#return True False
	if not all(passed):
		return 'Err:0'

