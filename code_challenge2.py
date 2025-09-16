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

nick = eval(input("Enter the amount to deposit --->  "))
print ("here is the breakdown of the deposit amount : ")
# b1 = nick // ni1   

b1 = nick // ni1
nick = nick % ni1
b2 = nick  // ni2
nick = nick % ni2
b3 = nick // ni3
nick = nick % ni3
b4 = nick // ni4
nick = nick % ni4
b5 = nick // ni5
nick = nick % ni5
b6 = nick // ni6
nick = nick % ni6
b7 = nick // ni7
nick = nick % ni7
b8 = nick // ni8
nick = nick % ni8
b9 = nick // ni9
nick = nick % ni9
b10 = nick // ni10
nick = nick  % ni10


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