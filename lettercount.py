string= input("Enter your word here: ")
char= input("Enter your character here: ")
i= 0
count= 0

while (i < len(string)):
    if (string[i] == char):
        count += 1
    i += 1
print("The number of times", char, "has occured is: ", count)