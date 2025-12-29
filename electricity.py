units= int(input("Enter the number of units used here:"))

if (units < 50):
    amount = units * 2.60
    charge = 25
elif (units <= 100):
    amount= 130 + ((units - 50)* 3.25)
    charge = 35
elif (units <= 200):
    amount= 130 + 162.50 + ((units - 100)* 5.26)
    charge = 45
else:
     amount= 130 + 162.50 + 526 +((units - 100)* 8.45)
     charge = 75
    
total= amount + charge

print(total)