num= int(input("Enter your number here: "))
power = len(str(num))
sum= 0
temp= num

while temp > 0:
    digit= temp % 10
    sum += digit**power
    temp //= 10
if num == sum:
    print("Your number is an armstrong number.")
else:
    print("Your number is not an armstrong number.")