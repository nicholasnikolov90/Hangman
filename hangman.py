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

def play(word):
    word = get_word(words)
    word_letters = set(word)
    lives = 11


    for i in range(len(word)+11):
        guess = input("Guess a letter: ")

        if guess in word:
            g_word += guess
            print(f"Your letter {guess}, is in the word")
            print(f"you have {lives} left, anad you have used these letters {p_guesses}")
            print(f"Your current word is: {c_word}")




play(word)