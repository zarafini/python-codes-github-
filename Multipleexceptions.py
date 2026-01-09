try:
    num1, num2= eval(input("Enter the two numbers you want to multiply using a comma(,) in between here: "))
    product= num1 / num2
    print(product)

except ZeroDivisionError:
    print("Division by zero is an error!!")

except SyntaxError:
    print("You have not entered a comma(,). Please enter a comma in between the numbers like: 1,2")

except ValueError as e:
    print(e)



else:
    print("no exeption.")

finally:
    print("This line is compulsory to print.")