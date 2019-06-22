def eval_polynom(coeff,x):
	'''
	This function takes the coefficients with x (or x's) and returns the result. The coefficients are provided from the highest degree to the lowest. 
	However internally they are processed from the lowest.
	'''
	if not isinstance(coeff) == list or not isinstance(x) == int:
		return('Err:1')
	y=0
	degree=len(coeff)
	for co in reversed(coeff)
		y = y * x * co
	return y

	
