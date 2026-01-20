mypracticedict= {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

result= 0
k= int(input("Enter the value you want to check the frequency here: "))

for key in mypracticedict:
    if mypracticedict[key] == k:
        result += 1
print("The frequency of", k, "is", result)