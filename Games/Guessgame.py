import random
from Score import add_score
#
# class Difficulty:
#   def __init__(self):
#     self.easy = 3
#     self.mid = 7
#     self.hard = 20
#
#
# newGame = Difficulty ()
# typeOfGame = input("which Difficulty u want ? 1/2/3 :")
#
# correctAnswer = False
# while correctAnswer == False:
#     if typeOfGame == "1":
#         difficulty = newGame.easy
#         correctAnswer = True
#     elif typeOfGame == "2":
#         difficulty = newGame.mid
#         correctAnswer = True
#     elif typeOfGame == "3":
#         difficulty = newGame.hard
#         correctAnswer = True
#     else:
#         print("please enter only 1/2/3 :")
#         typeOfGame = input("which Difficulty u want ? 1/2/3 ")


def generate_number(endRange):
    return random.randrange(1, endRange)

def get_guess_from_user(difficulty):
    guess_number = int(input("guess number between 1 to " + str(difficulty) + " :"))
    return guess_number

def main_guessGame(difficulty):
    secret_number = generate_number(difficulty)
    guess_number = 0
    tries = 0
    while guess_number!=secret_number:
        guess_number= get_guess_from_user(difficulty)
        tries+=1
        if guess_number == secret_number:
            print("Congratulations you did it in " + str(tries)+ " try")
        elif guess_number > secret_number:
            print("You guessed too high")
        elif guess_number < secret_number:
            print("You Guessed too small!")

    add_score(difficulty)
