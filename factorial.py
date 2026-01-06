x= int(input("Enter the number of which you its factorial here: "))

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x*factorial(x - 1)


print(factorial(x))