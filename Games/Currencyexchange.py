import random
from currency_converter import CurrencyConverter
from Score import add_score



def CurrencyRouletteGame(difficulty):
    c = CurrencyConverter()
    n = random.randint(0,100)
    generate_number = int(input('what is the value of  '+str(n) + " USD to ILS:"))
    print("generate number is: {}".format(generate_number))
    convert_total = c.convert(n, 'USD', 'ILS')
    print(convert_total)

    temp_low = generate_number - (5 - difficulty)
    temp_high = generate_number + (5 - difficulty)
    print(temp_low)
    print(temp_high)
    if temp_low < convert_total < temp_high:
        print("ok")
    else:
        print("not in range")
    add_score(difficulty)

