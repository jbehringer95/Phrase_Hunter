import random
from phrase import Phrase


class Game:
    
    def __init__(self):
        self.misses = 0
        self.phrases = [Phrase('Hello world'),
            Phrase('Just keep swimming'),
            Phrase('Get to the chopper'),
            Phrase('There is no place like home'),
            Phrase('May the force be with you')
            ]
        self.active_phrase = self.get_random_phrase()
        self.guesses = ['']

    def get_random_phrase(self):
        return random.choice(self.phrases)

    def welcome(self):
        print('Welcome to the the game of Phrase Hunter')

    def start(self):
        self.welcome()

        while self.misses < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(self.guesses)
            self.user_guess = self.get_guess()
            self.guesses.append(self.user_guess)
            if not self.active_phrase.check_guess(self.user_guess):
                self.misses += 1
            print('Misses: {}'.format(self.misses))
            print(self.active_phrase.display(self.guesses))

        self.game_over()

        

    def get_guess(self):
        x = input('Enter a letter: ')
        return x

    def game_over(self):
        if self.misses == 5:
            print('I am so sorry you did not win!')

        else:
            print('Awesome you was able to get the the phrase correct')





        
