#Enter 10 random numbers, then get the summation of all odd numbers

sum = 0

for n in range(1, 11, 1):
	value = int(input('Enter any number --> '))
	if value % 2:
		sum += value 
print("The sum of all the given odd numbers is", sum)