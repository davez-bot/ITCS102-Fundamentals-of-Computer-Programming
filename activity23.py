def greet(name):
    kamusta = "hello" + name
    print(kamusta)
greet(" Davez")  


def factoriel(num):
    fac = 1
    for x in range(num, 0, -1):
        fac *= num
    return fac
print("Output - ", factoriel(2))
print("Output - ", factoriel(5))


def box(num):
    for x in range(num + 1):
        for y in range(num + 1):
            if x == 0 or y == 0 or x == num or y == num:
                print(y, end= " ")
            else:
                print(" ", end=" ")
        print()
        
print(box(9))        
                        