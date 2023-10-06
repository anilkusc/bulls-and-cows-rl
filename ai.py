import random

class ArtificialIntelligence:
    def __init__(self, digit):
        self.digit = digit
        self.possible_numbers = [0,1,2,3,4,5,6,7,8,9]
    
    def predict_a_number(self):
        while True:
            random_number = random.randint(
                10**(self.digit-1), 10**self.digit)
            if self.isNumberValid(random_number):
                break
        return random_number
    
    def isNumberValid(self, prediction):
        if len(str(prediction)) != len(set(str(prediction))):
            return False
        if len(str(prediction)) != self.digit or prediction < 1:
            return False
        return True