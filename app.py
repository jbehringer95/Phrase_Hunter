from game import Game
from phrase import Phrase


if __name__ =='__main__':
    game =Game()
    game.start()

    while True:
        user_input = input('Would you like to play another game. y/n \n').lower()
        if user_input != 'n' and user_input != 'y':
            print('That is not an invalid option please put a y or n')

        elif user_input == 'y':
            game = Game()
            game.start()

        else:
            break
