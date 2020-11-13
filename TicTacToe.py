# Start with empty board
# X goes first
# then O goes
# they repeat this cycle until one wins or there are no spaces left


# while there is no winner or there are spaces left:
#     X moves
#     check if there is a winner
#     check if there are spaces left
#     O moves
#     check if there is a winner
#     check if there are spaces left

# How to make a move?

# Things to play tic tac toe
# 3 columns 3 rows = 9 spaces

# if choice >= 0 and choice <= 8:
#     if spaces[choice] == "X" or spaces[choice] == "O":
#         print("That spot is taken.")
#         validChoice = False
#     else:
#         validChoice = True
# else:
#     print("Pick a spot from 1 to 9")

spaces = [' '] * 9
for i in range(len(spaces)):
    spaces[i] = i + 1


def intInput(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except:
            print("Please enter an integer.")

def makeMove(player):
    currentPlayer = player
    validChoice = False
    while not validChoice:
        choice = intInput("Pick a spot: ") - 1
        try:
            if choice > 8 or choice < 0:
                print("Pick a number between 1 and 9")
                validChoice = False
            elif spaces[choice] == "X" or spaces[choice] == "O":
                print("That spot is taken.")
                validChoice = False
            else:
                validChoice = True
        except:
            print("Pick a number between 1 and 9")
    print(choice)

    spaces[choice] = currentPlayer

# spaces[0] = "X"
# print(spaces)
    board = f' {spaces[0]} | {spaces[1]} | {spaces[2]}\n' \
            f'-----------\n' \
            f' {spaces[3]} | {spaces[4]} | {spaces[5]}\n' \
            f'-----------\n' \
            f' {spaces[6]} | {spaces[7]} | {spaces[8]}'

    print(board)
# 2 players, X and O
# detect wins, and draws
