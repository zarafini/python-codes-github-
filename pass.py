# Write a program to satisfy the following conditions of the given range:
# 1. If the number is divisible by 20, it provides an output "twist." 
# 2. If the number is divisible by 15, it will pass (no output) 
# 3. If the number is divisible by 5, it will give an output “fizz.” 
# 4. If the number is divisible by 3, it will give an output "buzz." 
# 5.  Otherwise, it will give the output of that number.



number= int(input("Enter your number here: "))

for i in range(number):
    if i % 20 == 0:
        print("twist")
    elif i % 15 == 0:
        pass
    elif i % 5 == 0:
        print("fizz")
    elif i % 3 == 0:
        print("buzz")
    else:
        print(i)