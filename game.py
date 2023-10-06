import random
from ai import ArtificialIntelligence


class Game:
    def __init__(self, digit):
        if 0 < digit < 10:
            self.digit = digit
        else:
            print("Digit number must be between 0 and 10")
            exit()
        while True:
            random_number = random.randint(
                10**(self.digit-1), 10**self.digit)
            if self.isNumberValid(random_number):
                self.computer_number = random_number
                break
        self.winner = 0
        self.turn = 1
        self.AI = ArtificialIntelligence(self.digit)
        self.player_sequence = 1  # can be 1 or 2. 2 is computer 1 is human

    def start(self):
        while self.winner == 0:
            print("Turn: ", self.turn)
            if self.player_sequence == 1:
                self.humanPlays()
            else:
                self.computerPlays()

    def computerPlays(self):
        computer_prediction = self.AI.predict_a_number()
        print("Computer Prediction:", computer_prediction)
        while True:
            pluses = input("Please enter Bulls(+):")
            minuses = input("Please enter Cows(-):")
            total = (int(pluses)+int(minuses))
            if 0 <= total <= self.digit and int(pluses) > -1 and int(minuses) > -1:
                break
            print("Wrong feedback please correct...")

        if self.isWinner(pluses):
            print("Computer Wins. ")
            print("Prediction: ", computer_prediction)
            self.winner = 2
            input("Please press a key to start new game...")
        else:
            self.turn = self.turn + 1
            self.player_sequence = 1

    def humanPlays(self):
        prediction = 0
        while True:
            prediction = input("Please enter your prediction:")
            if self.isNumberValid(prediction):
                break
            print("Wrong prediction.Please retry...")

        pluses, minuses = self.calculatePrediction(prediction)
        if self.isWinner(pluses):
            print("Human Wins. ")
            print("Prediction: ", prediction)
            print("Computer Number: ", self.computer_number)
            self.winner = 1
            input("Please press a key to start new game...")
        else:
            self.turn = self.turn + 1
            self.player_sequence = 2
            print("###########################################################")
            print("Prediction: ", prediction)
            print("Bulls(+): ", pluses)
            print("Cows(-): ", minuses)
            print("###########################################################")

    def isNumberValid(self, prediction):
        if isinstance(prediction, str):
            if len(prediction) != self.digit:
                return False
            if int(prediction[0]) < 1:
                return False
        if len(str(prediction)) != len(set(str(prediction))):
            return False
        if len(str(prediction)) != self.digit or int(prediction) < 1:
            return False
        if int(str(prediction)[0]) == 0:
            return False
        return True

    def isWinner(self, pluses):
        if pluses == self.digit:
            return True
        return False

    def calculatePrediction(self, prediction_number):
        pluses = 0
        minuses = 0
        for i, digit in enumerate(str(prediction_number)):
            if int(digit) == int(str(self.computer_number)[i]):
                pluses = pluses + 1
            else:
                if digit in str(self.computer_number):
                    minuses = minuses + 1
        return pluses, minuses
