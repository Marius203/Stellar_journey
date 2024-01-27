from Board import Board


class Game():

    def __init__(self, board:Board):
        self.board = board
        self.how_many_enemies = 3
        self.board.create_board()
        self.board.add_endeavor()
        self.board.add_stars()
        self.board.add_Blingon(3)
        self.board.print_board()
        self.ok = 1

    def shoot(self, x, y):

        if self.board.board_unknown._rows[x-1][y] == "B":
            self.board.board_unknown._rows[x-1][y] = " "
            for i in range (0,8):
                for j in range (1,9):
                    if self.board.board_unknown._rows[i][j] == "B":
                        self.board.board_unknown._rows[i][j] = " "
            self.board.board._rows[x - 1][y] = " "
            for i in range(0, 8):
                for j in range(1, 9):
                    if self.board.board._rows[i][j] == "B":
                        self.board.board._rows[i][j] = " "
            self.board.no2 = self.board.no2[:self.how_many_enemies]
            self.how_many_enemies = self.how_many_enemies - 1
            self.board.add_Blingon(self.how_many_enemies)
            print(self.how_many_enemies)
            print(self.board.no2)
            print("You destroyed an enemy!")
        else:
            print("You missed!")

    def cheat(self):
        print(self.board.board_unknown)

    def warp(self, x, y):
        if self.board.board_unknown._rows[x-1][y] == "B":
            print("You Lost!")
            self.ok = 0

        elif self.board.board_unknown._rows[x-1][y] == "*":
            print("You would hit a star!!!!")
        else:
            if x-1 != self.board.e_coordinates[0][0] and y != self.board.e_coordinates[0][1] :
                print("invalid")

            else :
                self.board.board_unknown._rows[x-1][y] = "E"
                self.board.board._rows[x-1][y] = "E"
                self.board.board_unknown._rows[self.board.e_coordinates[0][0]][self.board.e_coordinates[0][1]] = " "
                self.board.board._rows[self.board.e_coordinates[0][0]][self.board.e_coordinates[0][1]] = " "
                self.board.e_coordinates[0][0] = x
                self.board.e_coordinates[0][1] = y
                print("You warped!")




# g = Game(Board())