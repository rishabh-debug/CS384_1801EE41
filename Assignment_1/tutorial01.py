# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	multiplication = num1 * num2
	return multiplication

# Function to divide two numbers 
def divide(num1, num2):
	if num2 == 0:
		print("Not define")
	elif type(num2) == type(num1) == type('a'):
		print("invalid input")
	else :
		division = num1/num2
		return division
	
def power(num1, num2):
	count = 1
	for i in range[0,num2]
		count *= num1
		return count

def printAP(a,d,n)
	AP = []
	for i in range[0,n]
	tn = [a + (n - 1) * d]
	AP.append(tn)
	return AP

