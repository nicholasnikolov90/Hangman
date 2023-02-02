import random
from words import words
import string

#working
def get_word(words):
    word = random.choice(words)
    #Remove any hyphenated or two word combos
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def play():
    word = get_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii.uppercase)
    used_letters = set()
    lives = 11

    user_letter = input('Guess a letter: ').upper()

    if user_letter in word_letters:
        used_letters.add(user_letter)

    else: lives = lives  - 1



    print(f"Your letter {guess}, is in the word")
    print(f"you have {lives} left, anad you have used these letters {p_guesses}")
    print(f"Your current word is: {c_word}")




play()