numbers1= [1, 2, 3]
numbers2= [4, 5, 6]


sum= map(lambda d, b, : d+b, numbers1, numbers2)
print(list (sum))



def square(n):
    return n*n

num= (2, 3, 4)

result= map(square, num)
print(list (result))