# Write a program to create a base class that consists of two functions: 
# one to display a value, and another function is an abstract method.
# Next, create a subclass that consists of a method similar to the abstract method.
# Finally, showcase how Abstraction is being implemented in this example.





from abc import ABC, abstractmethod

class abcclass(ABC):
    def printsmt(self, x):
        print("Passed value", x)

    @abstractmethod
    def task(self):
        print("We are inside abcclass task")

class testclass(abcclass):
    def task(self):
        print("We are inside testclass task")

obj= testclass()
obj.task()
obj.printsmt(100)