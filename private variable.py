variable=  int(input("Enter your integer here: "))
class private:
    __privateVar= variable
    
    def __privateMethod(self):
        print("I'm iniside the class 'private'.")

    def hello(self):
        print("Private Variable value is:", private.__privateVar)

obj1= private()
obj1.hello()
obj1.__privateMethod()