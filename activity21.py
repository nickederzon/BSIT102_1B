#while loop 
#laundry analogy
#keywords -- while, continue, break
#requirement - boolean variable

isDirty = True #boolean initial value
sum = 0
while isDirty == True:
	confirm = input("Do you wish to continue washing (yes / no)").lower()
	sum += 1
	if confirm =='yes':
		print("Washing continue....")
		continue
	else:
		print("Washing stop....")
		break
		
print("Number of cycle is", sum)