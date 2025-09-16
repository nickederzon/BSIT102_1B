print("Enter 7 numbers")

sum = 0

for n in range(1, 8, 1):
	value = eval(input("Enter any number --> "))
	if value % 2:
		sum += value 
print("The sum of all the given odd numbers is", sum)