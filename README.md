# Tic Tac Toe Game

## Description
This repository contains two implementations of the classic game Tic Tac Toe: one using a graphical user interface (GUI) with PyQt5 and the other using a command-line interface (CLI). Both versions allow two players to compete against each other, with the GUI version offering a more interactive experience.

## CLI Version

### Description
The CLI implementation allows a player to compete against a computer opponent in a console-based environment. The player can choose their moves by entering numbers corresponding to board positions.

### Features
- Text-based board display in the console
- Player vs. computer gameplay
- Validates player moves and announces the winner or a tie

### Code Overview
- The board is represented as a list of strings.
- `draw_board(board)` displays the current state of the game.
- `check_win(board, player)` checks if the specified player has won.
- `get_player_move(board)` prompts the player for their move.
- `get_computer_move(board)` randomly selects a move for the computer.

## GUI Version

### Description
The GUI implementation uses the PyQt5 library to create a windowed application where two players can take turns clicking on a 3x3 grid to place their symbols ("X" and "O"). The game checks for winners or ties after each turn and displays a message accordingly.

### Features
- Interactive 3x3 grid for gameplay
- Displays winner or tie messages using message boxes
- Resets the game after completion

### Code Overview
- The `TicTacToe` class manages the game logic and UI.
- `button_clicked(row, col)` updates the board and checks for a winner or tie.
- `check_winner(player)` checks if the current player has won.
- `is_board_full()` checks if the board is full, indicating a tie.
- `reset_game()` resets the game state for a new round.

