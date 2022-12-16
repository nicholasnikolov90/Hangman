import random
from words import words

#working
def get_word(words):
    word = random.choice(words)

    return word

def guessing(word):
    c_word = ""
    p_guesses = ""
    lives = 11


    for i in range(len(word)+11):
        guess = input("Guess a letter: ")

        if guess in word:
            g_word += guess
            print(f"Your letter {guess}, is in the word")
            print(f"you have {lives} left, anad you have used these letters {p_guesses}")
            print(f"Your current word is: {c_word}")




guessing(word)