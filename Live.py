def welcome():
    name = input("Please type your name: ")
    while name.isalpha() == False:
        print("Please use only letters! ")
        name = input("Please type your name: ")
    print(F"Hello {name} welcome to the World of Games (WoG).\nHere you can find many cool games to play")

def load_game():
    game = 0
    difficulty = 0
    print("Please choose a game to play: \n 1. Memory Game - a sequence of numbers will appear for 1 second and you have to  guess it back.\n 2. Guess Game - guess a number and see if you chose like the computer. \n 3. Currency Roulette - try and guess the value of a random amount of USD in ILS ")
    while game <1 or game >3 :
        print("Enter a number 1-3")
        try:
            game = int(input("Please choose a game: "))
        except:
            print("pls enter a number")
            game = 0
    print(" the chosen game is: ", game)
    while difficulty <1 or difficulty> 10:
        print("Enter a number 1-10")
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 10: "))
        except:
            print("pls enter a number")
    print(" the chosen difficulty is: ", difficulty)

    return game,difficulty