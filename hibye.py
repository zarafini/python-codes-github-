valid= False

while not valid:
    try:
        num= int(input("Enter your number here: "))
        while num % 2 == 0:
            print("Hi, Bye")
        valid= True
    except:
        print("Invalid.")