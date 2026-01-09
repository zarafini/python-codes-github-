amount= float(input("Enter your amount here: "))
paid= float(input("Enter the amount paid: "))

if amount == paid:
    print("You have paid the entire amount. You have no due.")
else:
    if amount < paid:
        print("You have paid extra.")
    else:
        print("You have", amount - paid, "amount due to pay.")
