#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.

myfirstdict= {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

result= 0
k= 2

for key in myfirstdict:
    if myfirstdict[key] == k:
        result += 1
print("The frequency of '2' is", result)