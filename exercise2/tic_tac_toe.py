# -*- coding: utf-8 -*-

"""
Jacqueline Xu
iXperience Tel Aviv
27 May 2019
Exercise 2: Tic-Tac-Toe
"""

#%%
"""
Exercise: Tic-Tac-Toe

We are going to build a program that allows us to play tic-tac-toe in the
terminal

In a nutshell, the tic-tac-toe board can be thought of 3 lists inside another
one

board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

For example, if we want to see what the status of the box above is left,
we can access doing board [[0,0]]

We have 2 players, and each player will alternate in choosing a different slot
on the board, and placing either an "X" (player 1) or "O" (player 2)

The game will have to validate that the new coordinates chosen by the current
player are valid, i.e., they need to be empty and be inside the board.


Hint: You can use a deque (in the module collections) to rotate between
player 1 and 2
"""

# prints out the board by printing '-' for all empty spaces
def print_board(board):
    print("board: ")
    print("  1 2 3")
    for i in range(len(board)):
        print(i+1, end = " ")
        for j in board[i]:
            print(j, end = " ")
        print()

# checks whether or not the board is full
def not_full(board):
    for i in board:
        for j in i:
            if (j == "-"):
                return True
    return False

# returns the player number at the location
def player_at(letter):
    if letter == 'X':
        return 1
    elif letter == 'O':
        return 2
    else:
        return 0
    
# checks if there is a winner
def winner(board):
    # check horizontally
    for i in board:
        if i[0] == i[1] and i[1] == i[2]:
            return player_at(i[0])
    # check vertically
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return player_at(board[0][i])
    # check diagonally
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
        (board[2][0] == board[1][1] and board[1][1] == board[0][2]):
        return player_at(board[1][1])
        return player_at(board[1][1])
    # no winner
    return 0

# prints instructions
def print_instructions():
    print("""
How To Play:
    1. Take turns as the instructions say
    2. Enter coordinate in the following manner: "a b" where a is
    which row (top row being 1) and b is which column (left
    column being 1))
          """)
    
def game():
    player = 0 
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
        ]
    print_instructions()
    print_board(board)
    
    while (not_full(board) and winner(board) == 0):
        if (player == 0):
            command = input('Player 1 (X) Command: ')
        else:
            command = input('Player 2 (O) Command: ')
        
        coordinates = command.split()
        
        # test for invalid coordinates
        if (len(coordinates) != 2):
            print("invalid number of arguments")
            continue
        if (len(coordinates[0]) != 1 or len(coordinates[1]) != 1):
            print("invalid argument types")
            continue

        # makes sure that the character is an integer between 0 and 2
        x = ord(coordinates[0]) - ord('0') - 1
        y = ord(coordinates[1]) - ord('0') - 1
        if (x < 0 or x > 2 or y < 0 or y > 2):
            print("invalid coordinates")
            continue
        
        # makes sure that the location is empty
        if (board[x][y] != "-"):
            print("location is already taken")
            continue
            
        # valid coordinates and may continue
        if (player == 0):
            board[x][y] = 'X'
        else:
            board[x][y] = 'O'
        print_board(board)
        player = ~ player # switch to other player
    
    print("Game Over!")
    win = winner(board)
    if (win != 0):
        print("Player {} wins!".format(win))

if __name__ == "__main__":
    game()
