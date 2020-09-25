from game import Game
from phrase import Phrase


if __name__ =='__main__':
    
    
    while True:
        game =Game()
        game.start()
        user_input = input('Would you like to play another game. y/n \n').lower()
        if user_input == 'n':
            break