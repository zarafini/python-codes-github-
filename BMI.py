weight= float(input("Enter your weight(in kg) here:"))
height= float(input("Enter your height(in cm) here:"))

BMI= weight / (height / 100)**2

print(BMI)

if BMI < 18.5:
    print("You are wnderweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are overweight.")
elif BMI <= 34.9:
    print("You are obese.")
elif BMI <= 39.9:
    print("You are very obese.")
else:
    print("You are severly obese.")