name =input("What is your name? -->")
fare =eval(input("your farefee? --->"))
person =input("Are you a student? (yes/no) -->")
if person =='yes':
	discount = fare * 0.20
	qfare = fare - discount
	print("Hi",name)
	print("Your discount is", discount)
	print("Your new fare is",qfare)
else:
	print("Sorry",name,"you are not eligible for a student discount")