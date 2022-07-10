import random
import time

from Score import add_score
from Utils import screen_cleaner


def generate_memorygame(difficulty):
    generate_sequence = []
    for i in range(0, difficulty):
        generate_sequence.append(random.randint(1, 101))
    print(generate_sequence)
    for i in range(4):
        time.sleep(0.7)
    return generate_sequence


# for i in range (0, 30):
#     print('')
# clear()

def main_MemoryGame(difficulty):
    screen_cleaner()
    generate_sequence = generate_memorygame(difficulty)
    for get_list_from_user in range(0, difficulty):
        time.sleep(2)
        screen_cleaner()
        print('enter number at index ' + str(get_list_from_user) + ":")
        num = int(input())
        if num == generate_sequence[get_list_from_user]:
            print('True')
        else:
            print('False')
            return
    add_score(difficulty)
