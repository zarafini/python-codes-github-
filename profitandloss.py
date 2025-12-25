costprice= int(input("Enter yout cost price:"))
sellingprice= int(input("Enter your selling price:"))

if sellingprice > costprice:
    print("It is a profit", sellingprice - costprice)
else:
    print("It is a loss", costprice - sellingprice)