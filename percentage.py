maths= int(input("enter your maths marks:"))
science= int(input("enter your science marks:"))
hindi= int(input("enter your hindi marks:"))
english= int(input("enter your english marks:"))

total= maths + science + hindi + english

print("the total marks that you got:", total)

percentage= total/400 * 100

print("the percentage of the total marks that you got:", int(percentage))