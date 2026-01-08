string= input("Enter your string here(capital letters only): ")

for i in string:
    if i == 'A':
        print(f"{i} is A")
        break
    else:
        print(f"{i} is not 'A'")