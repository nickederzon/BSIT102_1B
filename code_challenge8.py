#Create a program that prints the of a number entered by the user, using a simple for loop.
#Ask the user to input a number.Use a for loop to print the multiplication table from for that number.
# Format each line clearly (e.g., 5 x 1 = 5).

#This reinforces:
#Looping over a fixed range (range(1, 11, 1))
#Using the loop variable in calculations
#String formatting


print("Multiplicatio Table Maker")

number = eval(input("Enter a number: ---> "))

for nick in range(1, 11, 1):
    result = number * nick
    print(number, "n",nick,"=",result)