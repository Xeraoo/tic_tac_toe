#Tymoteusz Maj
#Github: Xeraoo

import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 'X'
computer = 'O'

def draw_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        try:
            move = int(move) - 1
            if move in range(9) and board[move] == ' ':
                return move
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Invalid input, try again.")

def get_computer_move(board):
    available_moves = [i for i in range(9) if board[i] == ' ']
    return random.choice(available_moves)

def main():
    while True:
        draw_board(board)
        move = get_player_move(board)
        board[move] = player
        if check_win(board, player):
            print("You win!")
            break
        move = get_computer_move(board)
        board[move] = computer
        if check_win(board, computer):
            print("Computer wins!")
            break
        if ' ' not in board:
            print("Tie!")
            break

if __name__ == '__main__':
    print("Below is a board designed for a game of tic-tac-toe, the boxes are numbered consecutively: ")
    print("1 - 2 - 3")
    print("4 - 5 - 6")
    print("7 - 8 - 9")
    print("\n")
    main()
