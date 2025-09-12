tem = eval(input("What is the temperature outside your location ---> "))
if tem <=0:
	print("Below Freezing")
elif tem >= 1 and tem <=15 :
	print("Extreme Cold Temperature")
elif tem >= 16 and tem <= 30 :
	print("Cold Temperature")
elif tem >= 31 and tem <= 38 :
	print("Lukewarm Temperature")
elif tem >= 39 and tem <= 42 :
	print("Warm Temperature")
elif tem >= 43 and tem <= 50 :
	print("Hot Temperature")
elif tem >= 51 and tem <= 60 :
	print("Extremly Hot Temperature")
elif tem >= 61 :
	print("Burning Temperature")
else:
	print("Invalid input, please try again")