size = int(input("Enter the Size ---> "))

for x in range(size + 1):
    for y in range(size + 1):
        if x + y == size or x == y:
            print("*", end = " ")
        else:
            print(" ", end = " ")    
    print()        
