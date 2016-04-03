def loadWords():
    """Return an alphabetical list of words"""

    print('\nLoading...')

    file = open('words.txt', 'r')
    wordlist = []
    for line in file:
        wordlist.append(line.strip().lower())
    return wordlist

def selectWord(list):
    """Choose a random word from 'list'"""

    import random
    return list[random.randint(0, len(list)-1)]

def welcome():
    """Print welcome message"""

    while (1):
        key = input('Welcome to Hangman! Press the \'Enter\' key to start the game.')
        if not key: break

def blanks(word):
    """Print blanks for the chosen word"""

    revealed = ''
    for i in range(len(word)):
        revealed += '_'
    return revealed

def revealLetters(word, letter, revealed):
    """Show blanks with revealed letters"""

    for i in range(len(word)):
        if word[i] == letter:
            revealed = addLetter(revealed, letter, i)
    print(revealed)
    return revealed

def addLetter(revealed, letter, index):
    """Replace '_' with reveled letter"""

    l = list(revealed)
    l[index] = letter
    return ''.join(l)

def showInfo(guesses, lives):
    """Print guessed letters and remaining lives"""

    print('Guessed letters: ', end='')
    print(*guesses, sep=', ')
    print('\nYou have', lives, 'lives remaining.')

def takeGuess():
    """Return single letter input"""
    guess = input('Enter your guess letter: ')
    return guess[0]    # first letter only

def hasWon(win, word):
    if win == 1:
        print('\nCongrats!!! The word was', word)
    else:
        print('\nYou lost. The word was', word)

def clrscr():
    """Clear console screen"""

    import os
    os.system('cls')
    # os.system('clear')


# Main Program
wordlist = loadWords()

welcome()

while (1):
    clrscr()

    word = selectWord(wordlist)

    revealed = blanks(word)

    lives = len(word) + 2
    win = 0
    guesses = []

    while (lives > 0 and win == 0):
        showInfo(guesses, lives)
        
        print(revealed)

        guess = takeGuess()
        guesses.append(guess)

        if guess in word:
            revealed = revealLetters(word, guess, revealed)
        else:
            lives -= 1

        if word == revealed:    # check for win
            win = 1

        clrscr()

    hasWon(win, word)

    replay = input('Do you want to play again? (y/n) ')
    if replay == 'n':
        break

