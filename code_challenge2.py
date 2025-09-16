ni1 = 1000
ni2 = 800
ni3 = 600
ni4 = 400
ni5 = 200
ni6 = 100
ni7 = 50
ni8 = 10
ni9 = 5
ni10 = 1

denum = eval(input("Enter the amount to deposit --->  "))
print ("here is the breakdown of the deposit amount : ")
# b1 = demun // ni1   

b1 = denum // ni1
denum = denum % ni1
b2 = denum  // ni2
denum = denum % ni2
b3 = denum // ni3
denum = denum % ni3
b4 = denum // ni4
denum = denum % ni4
b5 = denum // ni5
denum = denum % ni5
b6 = denum // ni6
denum = denum % ni6
b7 = denum // ni7
denum = denum % ni7
b8 = denum // ni8
denum = denum % ni8
b9 = denum // ni9
denum = denum % ni9
b10 = denum // ni10
denum = denum  % ni10


print(b1, "-", ni1)
print(b2, "-", ni2)
print(b3, "-", ni3)
print(b4, "-", ni4)
print(b5, "-", ni5)
print(b6, "-", ni6)
print(b7, "-", ni7)
print(b8, "-", ni8)
print(b9, "-", ni9)
print(b10,"-",ni10)