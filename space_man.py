import random

word = list()

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def find_indicies(str, find_char):
    '''given str (string) and a find_char (char)
    iterate through the string and return an array of indices 
    where that find_char is present'''
    indicies = []
    for index in range(len(str)):
        char = str[index]
        if char == find_char:
            indicies.append(index)
    return indicies


def find_indicies_for_char(str, find_char):
    '''alternate approach to find indicies '''
    indicies = []
    index = 0
    for char in str:
        if char == find_char:
            indicies.append(index)
        index += 1
    return indicies

def find_indicies_enumerate(str, find_char):
    '''alternate approach to find indicies using enumerate
    enumerate allows us to keep track of both the index and 
    the character we are up to '''
    indicies = []
    for index, char in enumerate(str):
        if char == find_char:
            indicies.append(index)
    return indicies







def user_input(prompt):
    user_input = input(prompt)
    while len(user_input) != 1 or not user_input.isalpha():
        # if the user input is one character
        if len(user_input) != 1:
            user_input = input("Please input one letter at a time: ")
        # if it is not a letter
        if not user_input.isalpha():
            user_input = input("Please input a letter: ")
    return user_input

def replace_blanks_with_letter(char, blanks, indicies):
    '''given a char, a list of blanks, and a list of indicies
    replace blanks with character at every index of indicies'''
    # secret_word = 'hello'
    # blanks = ['_','_','_','_','_',]
    # indicies = [2,3]
    # char = 'l'
    for update_index in indicies:
        # update blanks at index update_index w char
        blanks[update_index] = char
    return blanks 

def game():
    secret_word = load_word()
    blanks = ["_"] * len(secret_word)
    lives = 7
    guesses = []
    while lives > 0 and secret_word != ''.join(blanks):
        guess = user_input("Enter a letter: ") 
        while guess in guesses:
            guess = user_input("You already guessed that try again: ") 
        guesses.append(guess)
        indicies = find_indicies(secret_word, guess)    
        #if the letter is found 
        if len(indicies) > 0: 
            #  replace blanks with character guessed
            blanks = replace_blanks_with_letter(guess, blanks, indicies)
            # afirm user for correct answer
            print("Correct!" , guess , "is in the word!")
            print("".join(blanks))
            print("Lives:" , lives)
            print("Guesses:" , ", ".join(guesses))

        # the guess was incorrect
        else:
            lives -= 1
            print("Wrong!", guess , "is not in the word!")
            print("".join(blanks))
            print("Lives:" , lives)
            print("Guesses:" , ", ".join(guesses))

    if lives == 0:
        print("Game over!!! The secret word was " + secret_word + ".")
    else:
        print("Congratulations! You won the game!")
print("Welcome to space man! Try to guess the secret word by guessing different letters!")
game()


