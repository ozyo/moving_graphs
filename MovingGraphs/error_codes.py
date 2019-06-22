#This file will handle the error codes. 
class ErrorCodes():
	def __call__(self,msg):
		code=msg.split(':')[1]
		return(self.__codemeaning(code))

	def __codemeaning(self,code)
		codemeanings={
		0:'Unit tests have failed.'
		1:'The entered data type is not valid. Please check the help of the function called to learn about the correct data type.'
		}
		return(codemeanings[code])