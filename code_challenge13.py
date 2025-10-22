name =input("Enter your name ---> ")
print("ODD NUMBER SUMMATION, press 0 to stop")

nick = True
sum = 0
odd = "" #string

while nick == True:
	num = eval(input("Input a random number --->"))
	
	if num % 2 == 1:
		print("ODD NUMBER DETECTED, code continues ")
		sum += num
		odd += str(num) + " "
		continue
	elif num == 0:
		print("Program stops .!!!!")
		break
	else:
		if num % 2 == 0:
			print("EVEN NUMBER DETECTED, continue")
		else:
			print("Invalid input")
		continue
print(f"Hi {name}, The sum of all ODD NUMBER is {sum}")
print(f"ODD NUMBERS DETECTED INCLUDED THE ff {odd}")