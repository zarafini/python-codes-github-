start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []
even = []
odd = []

for i in range(start, end + 1):
    sq = i * i
    squares.append(sq)

    if sq % 2 == 0:
        even.append(sq)
    else:
        odd.append(sq)

print("\nAll square values:", squares)
print("Even square values:", even)
print("Odd square values:", odd)