class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter} ", end = "")
            else:
                print('_ ', end= "")


    def check_guess(self, guess):

        if guess in self.phrase:
            return True

        else:
            False

    def check_complete(self, guesses):
        for letters in self.phrase:
            if letters not in guesses:
                return False
        return True
