#Tymoteusz Maj
#Github: Xeraoo
#Zadanie 11

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QGridLayout


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kółko i krzyżyk")
        self.setGeometry(100, 100, 300, 300)

        self.current_player = "X"
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]

        self.buttons = []
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        for row in range(3):
            for col in range(3):
                button = QPushButton("", self)
                button.clicked.connect(lambda _, r=row, c=col: self.button_clicked(r, c))
                layout.addWidget(button, row, col)
                self.buttons.append(button)

        self.setLayout(layout)

    def button_clicked(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row * 3 + col].setText(self.current_player)

            if self.check_winner(self.current_player):
                QMessageBox.information(self, "Koniec gry", f"Wygrał gracz {self.current_player}!")
                self.reset_game()
            elif self.is_board_full():
                QMessageBox.information(self, "Koniec gry", "Remis!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            if '' in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        for button in self.buttons:
            button.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec_())
