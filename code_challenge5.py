for x in range(6, 0, -1):
    for y in range(1, x+1):
        print("*", end=" ")
    print()

print("\n============================\n")   

for x in range(1, 8):
    for y in range(1, x, 1):
        print(x, end=" ")
    print(x)
