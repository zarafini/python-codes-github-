a= int(input("Enter your number: "))

for i in range(1, a):
    if i % 5 == 0:
        continue
    print(i)