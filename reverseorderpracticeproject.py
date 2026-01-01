num= int(input("Enter the number of wich you want to find the length here: "))
length= len(str(num))
print("This number has", length, "number of characters.\n")






char= input("Enter your letter here: ")
char = char.lower()

if char in 'aeiou':
    print(char, "is a vowel.\n")
else:
    print(char, "is a consonant.\n")



len1= int(input("Enter the length of the first side of the triangle here: "))
len2= int(input("Enter the length of the second side of the triangle here: "))
len3= int(input("Enter the length of the third side of the triangle here: "))

if len1 == len2 == len3:
    print("Your triangle is and equilateral triangle.")
elif len1 == len2 != len3:
    print("Your triangle is and iscocles triangle.")
elif len1 != len2 == len3:
    print("Your triangle is and iscocles triangle.")
elif len1 == len3 != len2:
    print("Your triangle is and iscocles triangle.")
else:
    print("Your triangle is and scalene triangle.")