try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Error! Your age is not a positive number. Please restart and enter a positive number.")
    else:
        print("Age entered is valid.")

        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

except ValueError:
    print("Error! Your input is not valid")