import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    #make word into _s
    #append if letter is correct
    while attempts <= len(secret_word):
        secret_word.replace(" " , "_")
        if guess in secret_word:
            print(secret_word.replace('_', guess))
    return get_guessed_word


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    return guess in secret_word


Guesses = []


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''

    attempts = len(secret_word)
    #TODO: show the player information about the game according to the project spec
    print("Hello player, your secret word has " + str(len(secret_word)) + " letters and you have " + str(len(secret_word)) + " attempts to complete this game.")
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while attempts <= len(secret_word):
        guess = input("Please enter a single letter: ")
        if len(guess) > 1:
            print("Please only choose one letter and not more than one, please try again.")
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            print("You are correct please continue " + guess)
            get_guessed_word
        else:
            attempts = attempts - 1
            print("sorry you are incorrect you have " + str(attempts) + " attempts left.")
            get_guessed_word
    #TODO: show the guessed word so far
    if guess in secret_word:
        print(guess)
    #TODO: check if the game has been won or lost
    if attempts > len(secret_word):
        print("sorry you have lost the game")
    else:
        print("Congrats you have won the game" + secret_word)






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
