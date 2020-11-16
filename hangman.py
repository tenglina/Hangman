# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for e in secretWord:
        if e in lettersGuessed:
            temp = True
        else:
            return False 
    return temp 
        
            



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    partword = []
    for e in secretWord:
        if e in lettersGuessed:
            partword.append(e)
        elif e not in lettersGuessed:
            partword.append('_')
    return ''.join(partword)
        
        
            



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avl = ''
    import string 
    for e in string.ascii_lowercase :
        if e not in lettersGuessed:
            avl += e
    return avl 
            
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Number of letters in word:", len(secretWord))
    print ("you will have 1 guess per round, 8 rounds in total.")
    lettersGuessed =[]
    for n in range (1,9):
        if n == 8 or isWordGuessed(secretWord, lettersGuessed) == True:
            print ("game over!")
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print ('Yay! you won!')
                return 
            else:
                print ('You lost! better luck next time')
                print ('the word was:', secretWord)
                return 
        print ('Round', n)
        guess = input('your guess: ')
        guess = guess.lower()
        lettersGuessed.append(guess)
        if guess in secretWord :
            print ("yay! you are now one step closer to guessing the word")
        else:
            print ("uh oh! better luck next time!")
        print (getGuessedWord(secretWord, lettersGuessed))
        print ("available letters for guessing:", getAvailableLetters(lettersGuessed))
        
            







# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
