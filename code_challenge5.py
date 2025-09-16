print ("The Factorial Program")
number = eval(input("Enter any number --> "))
factorial = 1
for nick in range(number, 0, -1):
		factorial *= nick
print("The factorial of", number, " is ", factorial)