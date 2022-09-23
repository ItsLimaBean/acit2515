import random

class Game:
    def __init__(self, turns=10):
        self.secret_word = SecretWord()
        self.turns = turns
        self.tried_letters = []

    def play(self):
        won = False
        while self.turns > 0:
            won = self.play_one_round()
            if won:
                print("You win!")
                break

            print(f"{self.turns} remaining!")
        
        if not won:
            print(f"You lose! The word was {self.secret_word.word}")
            


    def play_one_round(self):
        letter = input(f"Enter a letter/word: ")
        input_len = len(letter)
        if input_len <= 0:
            print("Enter a letter/word")
            return self.play_one_round()
        
        
        if input_len == 1:
            letter = letter[0].upper()
            if letter not in self.tried_letters:
                self.tried_letters.append(letter)
            else:
                print("Already tried", letter)
                return self.play_one_round()

            self.turns -= 1

            print(self.secret_word.show_letters(self.tried_letters))
            return self.secret_word.check_letters(self.tried_letters)
        else:
            self.turns -= 1
            
            guessed_full = self.secret_word.check(letter)
            if not guessed_full:
                print("Incorrect guess")
            return guessed_full

        

class SecretWord:
    def __init__(self, word=None):
        if word is None:
            with open("words.txt", "r") as file:
                self.word = random.choice(file.read().splitlines())
        else:
            self.word = word
        
    def show_letters(self, letters):
        letters = [letter.upper() for letter in letters]
        return " ".join([ (letter.upper() if letter.upper() in letters else "_") for letter in self.word ])

    def check_letters(self, letters):
        for letter in self.word.upper():
            if letter.upper() not in letters:
                return False
        return True

    def check(self, word):
        return "".join([l.lower() for l in word]) == self.word

if __name__ == "__main__":
    my_game = Game(10)
    my_game.play()