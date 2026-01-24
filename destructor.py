# Write a program to create a class with the name employee.
# Create a constructor and destructor.
# Then, write a function to create an object for that class and delete the object.
# Make sure you call the function to get everything implemented.





class employee:
    def __init__(self):
        print("Employee created...")

def __del__(self):
        print("Destructor called...")

def Create_obj():
    print("Making object...")
    obj= employee()
    print("Function ending...")
    return obj

print("Calling Create_obj function...")
obj= Create_obj()
print("Program ending...")
print("your program has successfully ended.")