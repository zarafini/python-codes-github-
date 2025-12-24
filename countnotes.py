amount= int(input("please input your number here:"))
note1= amount//100
note2= (amount % 100)//50
note3= ((amount % 100) % 50)//10

print("number of 100 rupee notes", note1)
print("number of 50 rupee notes", note2)
print("amount of 10 rupee noted", note3)