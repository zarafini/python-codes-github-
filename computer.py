# class Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price).
# Now create an object for the class Computer.
# Try changing the value of max price and use the sell function to display the updated price.
# Use a setter function to update the value and again display the price.





class Computer:
    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print("Selling Price: {}".format(self.__max_price))

    def set_max_price(self, price):
        self.__max_price= price

comp= Computer()

comp.__max_price= 1000

comp.set_max_price(1000)
comp.sell()