from Board import Board
from Game import Game
class Player_Interface():
    def __init__(self, game:Game):
        self.game = game

    def start(self):
        while True:
            if self.game.how_many_enemies == 0:
                print ("You won")
                break
            print("What do you want to do?")
            print("1. Shoot")
            print("2. Warp")
            print("3. Cheat")
            print("4. Quit")
            choice = input("Your choice: ")
            if choice == "Shoot":
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                self.game.shoot(x, y)
                self.game.board.print_board()

            elif choice == "Cheat":
                self.game.cheat()

            elif choice == "Warp":
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                self.game.warp(x, y)
                if self.game.ok == 0:
                    break

            elif choice == "Quit":
                break
            else:
                print("Wrong input!")

if __name__ == '__main__':
    p = Player_Interface(Game(Board()))
    p.start()