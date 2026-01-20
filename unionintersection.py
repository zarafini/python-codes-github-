# Write a program to find the intersection of two sets.
# Set1 = {green, blue} Set2 = {blue, yellow}


Set1 = {"green", "blue"}
Set2 = {"blue", "yellow"}

set3= Set1.intersection(Set2)
print(set3)

set4= Set1.union(Set2)
print(set4)

set5= Set1.symmetric_difference(Set2)
print(set5)