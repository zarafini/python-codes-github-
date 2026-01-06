number= int(input("Enter your number here: "))
def cube(number):
    return number*number*number

def divisible(number):
    if number % 3 == 0:
        print("Your number is divisible by 3.")
        return cube(number)
    else:
        return False
    
print(divisible(number))
print("Your number's cube is:", cube(number))