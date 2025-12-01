for nick in range(1,10,1):
    for x in range(10,nick,-1):
        print(" ", end=" ")
    for y in range(1,nick,1):
        print("x", end=" ")
    for go in range(1,nick,1):
        print("x", end=" ")
    print()

for nick in range(1,11,1):
    for x in range(1,nick,1):
        print(" ", end=" ")
    for y in range(10,nick,-1):
        print("x", end=" ")
    for go in range(10,nick,-1):
        print("x", end=" ")
    print()