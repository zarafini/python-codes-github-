marks1= int(input("Enter your marks here:"))
marks2= int(input("Enter your marks here:"))
marks3= int(input("Enter your marks here:"))
marks4= int(input("Enter your marks here:"))
marks5= int(input("Enter your marks here:"))

total= marks1 + marks2 + marks3 + marks4 + marks5
average= total/5

if average >= 91 and average <= 100:
    print("You got A1.")
elif average >= 81 and average < 91:
    print("You got A2.")
elif average >= 71 and average < 81:
    print("You got B1.")
elif average >= 61 and average < 71:
    print("You got B2.")
elif average >= 51 and average < 61:
    print("You got C1.")
elif average >= 41 and average < 51:
    print("You got C2.")
elif average >= 31 and average < 41:
    print("you got D1.")
elif average >= 21 and average < 31:
    print("You got D2.")
else:
    print("You failed.")