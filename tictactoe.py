board= [""] *9
player= "X"


def show():
    print("\n".join([
        f"{board[0]}|{board[1]}|{board[2]}",
        "-+-+-",
        f"{board[3]}|{board[4]}|{board[5]}",
        "-+-+-",
        f"{board[6]}|{board[7]}|{board[8]}"
    ]))
    print()

def win(p):
    combos= [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in combos)

for _  in range(9):
    show()
    move= int(input(f"Player {player}, choose (1-9): ")) - 1

    if board[move] != "":
        show()
        print("Taken! Try again.")
        continue

    board[move] = player

    if win(player):
        show()
        print(f"Player {player} wins!")
        break

    player = "0" if player == "X" else "X"
else:
    show()
    print("Draw")