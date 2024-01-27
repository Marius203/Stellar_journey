from prettytable import PrettyTable
import random

class Board():

    def __init__(self):
        self.board = PrettyTable()
        self.board_unknown = PrettyTable()
        self.no = []
        self.no2 = []
        self.e_coordinates = []


    def create_board(self):
        self.board.field_names = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.board.add_row([""] * 9)
        for i in range(8):
            self.board._rows[i][0] = i+1

        self.board_unknown.field_names = [" ", "A", "B", "C", "D", "E", "F", "G", "H"]
        for i in range(8):
            self.board_unknown.add_row([""] * 9)
        for i in range(8):
            self.board_unknown._rows[i][0] = i + 1

    def print_board(self):
        print(self.board)

    def add_endeavor(self):
        x = random.randint(0,7)
        y = random.randint(1,8)
        self.board._rows[x][y] = "E"
        self.board_unknown._rows[x][y] = "E"
        self.no2.append([x,y])
        self.no.append([x,y])
        self.e_coordinates.append([x,y])

    def add_stars(self):
        i = 0
        while i < 10:
            a = random.randint(0,7)
            b = random.randint(1,8)
            if self.board._rows[a][b] == "E" or [a,b] in self.no:
                pass
            else:
                self.board._rows[a][b] = "*"
                self.board_unknown._rows[a][b] = "*"
                i = i + 1
                self.no2.append([a, b])
                self.no.append([a, b])
                self.no.append([a+1, b])
                self.no.append([a-1, b])
                self.no.append([a, b+1])
                self.no.append([a, b-1])
                self.no.append([a-1, b-1])
                self.no.append([a-1, b+1])
                self.no.append([a+1, b-1])
                self.no.append([a+1, b+1])

    def add_Blingon(self, n):
        i = 0
        while i < n:
            a = random.randint(0,7)
            b = random.randint(1,8)
            if self.board_unknown._rows[a][b] != "E" and [a,b] not in self.no2:
                self.board_unknown._rows[a][b] = "B"
                i = i + 1
                self.no2.append([a, b])
                if abs(self.e_coordinates[0][0] - a) <= 1 and abs(self.e_coordinates[0][1] - b) <= 1:
                    self.board._rows[a][b] = "B"


#
# b = Board()
# b.create_board()
# b.add_endeavor()
# b.add_stars()
# b.add_Blingon(3)
# b.print_board()