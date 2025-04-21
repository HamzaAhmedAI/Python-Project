import random 
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)    # randomly choose something from the list
    while "__" in words or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in th word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    #getting user input 
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print('You have already used that character. please try again. ')
    
    else:
        print('invalid character. Please try again.')


user_input = input('Type something:')
print(user_input)