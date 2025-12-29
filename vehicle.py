print("What vehicle do you want to ride?(Please enter the option numbers.)")
print("1. Car")
print("2. Bike")

choice= int(input("Enter your choice here:"))

if choice == 1:
    print("Which type of car would you like?")
    print("1. 5 seater car.")
    print("2. 7 seater car.")
    print("3. EV.")
    carchoice= int(input("Enter your choice here:"))
    if carchoice == 1:
        print("You have successfully booked a 5 seater car.")
    elif carchoice == 2:
        print("You have successfully booked a 7 seater car.")
    else:
        print("You have successfully booked an EV.")
else:
    print("Which type of bike would you like?")
    print("1. Scooty.")
    print("2. Scooter.")
    print("3. Motercycle.")
    bikechoice= int(input("Enter your choice here:"))
    if bikechoice == 1:
        print("You have successfully booked a scooty.")
    elif bikechoice == 2:
        print("You have successfully booked a scooter.")
    else:
        print("You have successfully booked a motercycle.")