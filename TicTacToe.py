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
    #print(choice)

    spaces[choice] = currentPlayer

# spaces[0] = "X"
# print(spaces)
    board = f' {spaces[0]} | {spaces[1]} | {spaces[2]}\n' \
            f'-----------\n' \
            f' {spaces[3]} | {spaces[4]} | {spaces[5]}\n' \
            f'-----------\n' \
            f' {spaces[6]} | {spaces[7]} | {spaces[8]}'

    print(board)


def isDraw():
    draw = False
    # draw if every space is full
    fullSpaces = 0
    for space in spaces:
        if space == "X" or space == "O":
            fullSpaces += 1
    #print(fullSpaces)
    if fullSpaces == 9: return True
    else: return False


def isAWinner():
    # check horizontal
    if spaces[0] == spaces[1] == spaces[2]:
        return True
    elif spaces[3] == spaces[4] == spaces[5]:
        return True
    elif spaces[6] == spaces[7] == spaces[8]:
        return True
    # check vertical
    elif spaces[0] == spaces[3] == spaces[6]:
        return True
    elif spaces[1] == spaces[4] == spaces[7]:
        return True
    elif spaces[2] == spaces[5] == spaces[8]:
        return True
    # check diagonals
    elif spaces[0] == spaces[4] == spaces[8]:
        return True
    elif spaces[2] == spaces[4] == spaces[6]:
        return True
    # otherwise there is no winner yet
    else:
        return False


spaces = [' '] * 9
for i in range(len(spaces)):
    spaces[i] = i + 1
winner = "Nobody"
board = f' {spaces[0]} | {spaces[1]} | {spaces[2]}\n' \
        f'-----------\n' \
        f' {spaces[3]} | {spaces[4]} | {spaces[5]}\n' \
        f'-----------\n' \
        f' {spaces[6]} | {spaces[7]} | {spaces[8]}'
print(board)
while True:
    makeMove("X")
    if isAWinner():
        winner = "X"
        break
    if isDraw():
        break
    # check for win/draw
    makeMove("O")
    if isAWinner():
        winner = "O"
        break
    if isDraw():
        break
print(f"{winner} wins!")
input()
