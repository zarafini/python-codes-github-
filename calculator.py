def add(x,y):
    return x + y

def subtract(r,s):
    return r - s

def multiply(p,q):
    return p * q

def divide(a,b):
    return a / b

print("Please select your operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")

choice= int(input("Enter your operation here: "))
num1= int(input("\nEnter your first number: "))
num2= int(input("Enter your second number: "))

if choice == 1:
    print("Your answer is:", add(num1, num2))
elif choice == 2:
    print("Your answer is:", subtract(num1, num2))
elif choice == 3:
    print("Your answer is:", multiply( num1, num2))
else:
    print("Your answer is:", divide(num1, num2))