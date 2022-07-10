import Live
import MemoryGame
import Guessgame
import Currencyexchange


name = Live.welcome()
game, difficulty = Live.load_game()

if game == 2 :
    Guessgame.main_guessGame(difficulty)
elif game ==1 :
   MemoryGame.main_MemoryGame(difficulty)
elif game ==3:
    Currencyexchange.CurrencyRouletteGame(difficulty)





