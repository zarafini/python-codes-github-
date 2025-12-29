medicalcause= input("Do you have a medical cause for this exam?(pls write 'Y'for yes and 'N' for no.):")
atendancenumber= int(input("Enter your atendance number here:"))

if medicalcause == 'Y':
    print("You are eligible for this exam.")
else:
 if atendancenumber >= 75:
    print("You are eligible for this exam.")
 else:
    print("You are not eligible for this exam.")