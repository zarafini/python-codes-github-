n= int(input("Enter the number of rows here: "))
va= 1

for i in range(1, n + 1):
    for j in range(i):
        print(va, end= "")
        va += 1
    print()