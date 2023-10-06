from game import Game

while True:
    print("Game is starting...")
    digit = input("Please input game digit: ")
    game = Game(int(digit))
    game.start()