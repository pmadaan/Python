class Connect4:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = [[0 for i in range(self.columns)] for j in range(self.rows)]
        self.winner = None
        self.turns = 0
    
    def play(self):
        player = 1
        self.displayBoard()
        while self.turns < self.rows * self.columns:
            column, row = self.prompt()
            self.turns += 1
            self.board[row][column] = player

            self.displayBoard()
            self.evaulate()
            if self.winner:
                print(f"Winner: Player {player}")
                break

            if player == 1:
                player = 2
            else:
                player = 1

        if not self.winner:
            print("Draw")


    def evaulate(self):
        for row in self.board:
            self.check_list(row)
            if self.winner:
                return
            
    
        for i in range(self.columns):
            column = [row[i] for row in self.board]
            self.check_list(column)
            if self.winner:
                return
            

        for i in range(self.rows):
            diagonal = []

            for j in range(self.columns):
                diagonal.append(self.board[i+j][i+j])

            
            self.check_list(diagonal)
            if self.winner:
                return

    def findDiagonal(self, row, column):
        dia = [self.board[row][column]]
        for i in range(0, self.rows-rows):
            dia.append(self.board[row+i][column+i])
        return dia

    def check_list(self, line):
        for i in range(len(line)-3):
            if all([cell == line[i] for cell in line[i:i+4]]):
                if line[i]:
                    self.winner = line[i]
                    return


    def displayBoard(self):

        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(str(self.board[i][j]))
            print(" ".join(row))

    def prompt(self):
        while True:
            column = input("Please select a column (1 to 7): ")

            if column.isdigit() and int(column) >= 1 and int(column) <=7:
                col_int = int(column)-1
                row = -1
                for i in range(self.rows-1, -1, -1):
                    if not self.board[i][col_int]:
                        row = i
                        break
                if row == -1:
                    print("Invalid input.")
                    continue

                return col_int, row

            print("Invalid input.")


game = Connect4()
game.play()