# Also, find the largest and the smallest number in the list.

li= [1, 4, 7, 0]

count= 0

for i in li:
    count= count + i

print(count)

b= len(li)

avg= count/b

print(avg)

li.sort()

print("Highest", li[-1])
print("Lowest", li[0])