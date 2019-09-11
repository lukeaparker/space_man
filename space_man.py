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

def game():
    secret_word = load_word()
    blanks = ["_"] * len(secret_word)
    lives = 7

    user_input("Enter a letter") 
    print(word)       
                
print("Welcome to space man! Try to guess the secret word by guessing different letters!")
game()


