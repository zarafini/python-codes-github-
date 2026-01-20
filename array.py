# Write a program to create an array with the following elements - [1, 3, 5, 3, 7, 9, 3].
# Then find the number of occurrences of number 3 in the array.
# Also, print the reversed array.

array1= 1, 3, 5, 3, 7, 9, 3

array2= array1.count(3)
print(array2)

print(str(array1)[:: -1])