def circumference(radius):
    π = 3.14
    return int(2*π*radius)

rad = float(input("Enter the radius of the circle: "))
answer = circumference(rad)
print("The circumference of the circle is:", answer)