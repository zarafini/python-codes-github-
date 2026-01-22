num= int(input("Enter a number: "))
odd= [i for i in range(1, num) if i % 2 != 0]
even= [i for i in range(1, num) if i % 2 == 0]

print("Odd numbers are:", odd)
print("Even numbers are:", even)



fruits = ["apple", "banana", "mango", "grapes"]
updatedfruits = [fruit.capitalize() for fruit in fruits]

print("Updated fruits list:", updatedfruits)