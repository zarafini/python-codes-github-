# 1. Create a class variable species
# 2. Create a __init__ method that has instance variables - name and age
# 3. Create instances of class Parrot, passing arguments as well
# 4. Print Class variable by accessing it
# 5. Print Instance variables as well




class Parrot:
    species= "bird"
    def __init__(self, name, age):
        self.name= name
        self.age= age

ob= Parrot("Polly", 7)
print("The parrot's name is", ob.name)
print("Polly's age is", ob.age)
print("Polly is a", ob.species)