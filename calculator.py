from calculator_art import logo 
cont = True

def calc(num1, num2,operator):
	if(operation == "+"):
		return num1+num2		
	elif(operation == "-"):
		return num1-num2
	elif(operation == "*"):
		return num1*num2
	else:
		if(num2==0):
			return "Infinity"
		elif(num1==0):
			return 0
		else:
			return num1/num2
	
while(cont):
	print(logo)
	print("Welcome to the calculator ")
	num1 = int(input("Enter the first number: "))
	print("+ \n-\n*\n/")
	cont2 =True
	while(cont2):	
		print("+ \n-\n*\n/")
		operation = input("Pick an operation: ")
		num2 = int(input("Enter the second number: "))
		result = calc(num1,num2,operation)
		print(f"{num1} {operation} {num2} = {result}")
		Repeat = input(f"Type 'y' if you want to continue with {result}, or type 'n' to start a new calculation: ")
		if(Repeat =="y"):
			cont2= True
		else:
			cont2 =False