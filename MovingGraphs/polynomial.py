def eval_polynom(coeff,x):
    '''
    This function takes the coefficients with x (or x's) and returns the result. The coefficients are provided from the highest degree to the lowest.
    '''
    if not isinstance(coeff,list) or not isinstance(x,int):
        return('Err:1')
    y=None
    for co in coeff:
        if y is None:
            y=co
        else:
            y = x * y + co
    return y

	
