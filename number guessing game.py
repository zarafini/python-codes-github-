import random

def game():
    computer= random.randint(1, 10)
    guess= None
    attempts= 0

    print("Welcome to number guessing game.")
    print("I am thinking of a number between 1 to 10")

    while guess != computer:
        try:
            guess= int(input("Enter your guess: "))
            attempts += 1
            if guess < computer:
                print("Too Low")
            elif guess > computer:
                print("Too High")
            else:
                print(f"You Win!")
        except ValueError:
            print("Enter a valid integer")

if __name__ ==  "__main__":
    game()