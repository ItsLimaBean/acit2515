"""
ACIT2515 Lab

Week 2 -- complete this file!

"""

import random

# The number of turns allowed is a global constant
NB_TURNS = 10

def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    words = []
    with open("words.txt", "r") as f:
        words = f.read().splitlines()
    return words[random.randrange(0, len(words)-1)]

def show_letters_in_word(word, letters):
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    letters = [letter.upper() for letter in letters]
    return " ".join([ (letter.upper() if letter.upper() in letters else "_") for letter in word ])

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""
    for letter in word.upper():
        if letter.upper() not in letters:
            return False
    return True

def main(turns):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the show_letters_in_word function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    word = pick_random_word()
    tried_letters = []
    found_all = False
    while turns > 0:
        letter = input(f"{turns} turns left | Enter a letter: ")
        if len(letter) <= 0:
            print("Enter a letter")
            continue

        letter = letter[0].upper()
        if letter not in tried_letters:
            tried_letters.append(letter)
        else:
            print("Already tried", letter)
            continue
        
        turns -= 1

        print(show_letters_in_word(word, tried_letters))
        if all_letters_found(word, tried_letters):
            found_all=True
            break
        
    
    print("You win!" if found_all else f"You lose! The word was {word}.")


if __name__ == "__main__":
    main(NB_TURNS)