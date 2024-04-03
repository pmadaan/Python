class TicTacToe:
    def __init__(self):
        rows, cols = (3, 3) 
        self.board = [[0 for i in range(cols)] for j in range(rows)] 
        self.game_over = False
        self.winner = 0
        self.turns = 0

    def play(self):
        char = 'x'

        while True:
            print("Enter the position (row & column) where you want to place " + char)
            self.display_board()
            row = int(input())
            column = int(input())

            if row > 3 or column > 3 or self.board[row-1][column-1]:
                print("Invalid input")
                continue
        
            self.turns += 1
            
            if char == 'x':
                self.board[row-1][column-1] = 1
                char = 'o'
            else:
                self.board[row-1][column-1] = 2
                char = 'x'
            
            self.evaluate()
            
            if self.game_over:
                print("Game Over")
                if self.winner:
                    print("Winner: Player " + str(self.winner))
                return

    def display_board(self):
        for row in self.board:
            board_row = []
            for i in range(3):
                if row[i] == 1:
                    board_row.append("x")
                elif row[i] == 2:
                    board_row.append("o")
                else:
                    board_row.append("-")
            print(" ".join(board_row))

    
    def evaluate(self):
        for row in self.board:
            if row[0] == row[1] == row[2]:
                if row[0]:
                    self.game_over = True
                    self.winner = row[0]
                    return

        for i in range(3):
            column = [row[i] for row in self.board]
            if column[0] == column[1] == column[2]:
                if column[0]:
                    self.game_over = True
                    self.winner = column[0]
                    return

        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[0][2] == self.board[1][1] == self.board[2][0]):
            if self.board[1][1]:
                self.game_over = True
                self.winner = self.board[1][1]
                return

        if self.turns == 9:
            print("Board Full")
            self.game_over = True
        


game = TicTacToe()
game.play()
