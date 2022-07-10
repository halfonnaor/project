import os
# The scores file at this point will consist of only a number.
# That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5

from Utils import SCORES_FILE_NAME as fileName

file = fileName

def add_score(difficulty):
    try:
        #take the score from Utils
        my_file = open(file)
        score = int(my_file.read())
    except:
        #if in not file, create
        my_file = open(file, "x")
        my_file.write("0")
        my_file.close()
        score = 0
    os.remove(file)
    my_file = open(file,"x")
    newScore = score + (difficulty * 3 + 5)
    my_file.write(str(newScore))


