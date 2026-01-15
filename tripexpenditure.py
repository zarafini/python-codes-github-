print("The cost for each night at this hotel will be rupees 1000.")
nights= int(input("Enter the number of nights you will be staying at this hotel here: "))

def hotel(nights):
    return nights * 1000

print("The amount for your stay:",hotel(nights))

plane= input("\nWould you like a one way ticket or two way ticket(if you choose the two way ticket, you get 25% OFF!!!): ")

if plane == 'one way ticket' or 'one way' or '1 way ticket' or '1 way':
    print("\nWe have the following places to go if you choose the one ticket: ")
    print("1. Kerala")
    print("2. Andaman Islands")
    print("3. Kashmir")
    print("4. Goa")
    place= input("\nEnter where you want to go here: ")

    if place == 1 or 'Kerala':
        price= 1000
        print("The price for your plane is: 1000")

    elif place == 2 or 'Mumbai':
        price= 1000
        print("The price for your plane is: 1000")

    elif place == 3 or 'Kashmir':
        price= 1000
        print("The price for your plane is: 1000")

    elif place == 4 or 'Goa':
        price= 1000
        print("The price for your plane is: 1000")

else:
    print("\nWe have the following places to go if you choose the two way ticket: ")
    print("1. Delhi")
    print("2. Mumbai")
    print("3. Agra")
    print("4. Goa")
    place= input("\nEnter where you want to go here: ")

    if place == 1 or 'Delhi':
        price= 1500
        print("The price for your plane is: 1500")

    elif place == 2 or 'Mumbai':
        price= 1500
        print("The price for your plane is: 1500")

    elif place == 3 or 'Agra':
        price= 1500
        print("The price for your plane is: 1500")

    elif place == 4 or 'Goa':
        price= 1500
        print("The price for your plane is: 1500")

def totalbill():
    return hotel(nights) + price

print("Your total bill is:", totalbill())