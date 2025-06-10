#Connect 4
import random

"""
    |A|B|C|D|E|F|G|
1)  | | | | | | | |
2)  | | | | | | | |
3)  | | | | | | | |
4)  | | | | | | | |
5)  | | | | | | | |
6)  | | | | | | | |
"""

def create_board():
    return [[" " for _ in range(7)] for _ in range(6)]

def show_board(board):

    updated_display_board = [[cell for cell in row] for row in board]
    header = "|A|B|C|D|E|F|G|"

    print(header)
    print("---------------")

    for row in updated_display_board:
        for i in range(len(row)):
            if row[i] == "Y":
                row[i] = "\033[33;1m" + "o" + "\033[0m"
            elif row[i] == "R":
                row[i] = "\033[31;1m" + "o" + "\033[0m"

    for row in updated_display_board:
        print("|"+row[0] + "|" + row[1] + "|" + row[2]+ "|" + row[3]+ "|" + row[4] + "|" + row[5] + "|" + row[6] + "|")
    print("---------------")

    return board

def show_hidden_board(board):
    header = "|A|B|C|D|E|F|G|"

    # Create a new board with independent nested lists
    updated_hidden_board = [[cell for cell in row] for row in board]
    print(header)
    print("---------------")

    for row in updated_hidden_board:
        print("|"+row[0] + "|" + row[1] + "|" + row[2]+ "|" + row[3]+ "|" + row[4] + "|" + row[5] + "|" + row[6] + "|")
    print("---------------")
    
    return board

def drop_input():
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    letters = "ABCDEFGabcdefg"
    while True:
        player_input = input(bold_start + "Pick a column to drop coin: " + bold_end)
        print("\n")
        if player_input == "restart" or player_input == "Restart":
            False
            return None
        elif player_input not in letters or len(player_input) > 1:
            print("Your input was incorrect, try again. \n")
            True
        else:
            False
            return column_letter_to_num(player_input)

def column_letter_to_num(letter):
    columns = ["Aa", "Bb", "Cc", "Dd", "Ee", "Ff", "Gg"]
    for i in range(len(columns)):
        if letter in columns[i]:
            column_num = i
    return column_num

def player_assignment():
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    yellow = random.randint(1,2)
    red = 0

    if yellow == 1:
        red = 2
        print("New game, " + "\033[33;1m" + "Yellow" + "\033[0m" + bold_start + " goes first" + bold_end)
        return "yellow"
    else:
        red = 1
        print("New game, " + "\033[31;1m" + "Red" + "\033[0m" + bold_start + " goes first" + bold_end)
        return "red"

def change_board(board, player_turn, column_num):
    if player_turn == "red":
        coin = "R"
    elif player_turn == "yellow":
        coin = "Y"

    # Create a new board with independent nested lists
    updated_board = [[cell for cell in row] for row in board]

    for i in range(len(updated_board) - 1, -1, -1):  # Start from the last row and move upwards
        if updated_board[i][column_num] == " ":
            updated_board[i][column_num] = coin  # Place the coin in the first empty spot
            break  # Stop after placing the coin
    
    return updated_board

def play_game():
    while True:
        starting_board = create_board()  # <-- reset the board every loop
        print("")
        show_board(starting_board)
        player_turn = player_assignment()

        column_num = drop_input()
        if column_num is None:  # Restart condition
            print("Restarting the game...\n")
            continue
        updated_board = change_board(starting_board, player_turn, column_num)
        # show_hidden_board(updated_board)
        print("\n")
        show_board(updated_board)
        
        if player_turn == "red":
            player_turn = "yellow"
        elif player_turn == "yellow":
            player_turn = "red"

        while True:
            if win_condition(updated_board, "Y") is True:
                print("\033[33;1m" + "Yellow" + "\033[0m" + " wins!!!!!!!!!!!!!!!!!!" + "\n")
                break
            elif win_condition(updated_board, "R") is True:
                print("\033[31;1m" + "Red" + "\033[0m" + " wins!!!!!!!!!!!!!!!!!!" + "\n")
                break
            elif check_full(updated_board) is True:
                print("\033[1m" + "It's a tie! No winner." + "\033[0m" + "\n")
                break

            if player_turn == "red":
                print("\033[31;1m" + "Red's" + "\033[0m" + " turn")
            else:
                print("\033[33;1m" + "Yellow's" + "\033[0m" + " turn")

            column_num = drop_input()
            if column_num is None:  # Restart condition
                print("Restarting the game...\n")
                break
            
            updated_board = change_board(updated_board, player_turn, column_num)
            # show_hidden_board(updated_board)
            print("\n")
            show_board(updated_board)
            if player_turn == "red":
                player_turn = "yellow"
            elif player_turn == "yellow":
                player_turn = "red"

def win_condition(board, piece):
    for r in range(len(board)): #Checks the horizontal
        for c in range(len(board[0]) - 3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    
    for r in range(len(board) - 3): #Checks the verticle
        for c in range(len(board[0])):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    for r in range(len(board) - 3):  #Check diagonal down-right
        for c in range(len(board[0]) - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    for r in range(3, len(board)): # Check diagonal up-right
        for c in range(len(board[0]) - 3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

def check_full(board):
    for r in range(len(board)):
        for s in range(len(board[r])):
            if board[r][s] == " ":
                return False
    return True

play_game()


