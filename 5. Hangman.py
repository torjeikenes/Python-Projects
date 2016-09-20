from random import randint
#list with different hangman stages
hangmanPics = ['''
 +---+
 |   |
 |
 |
 |
 |
=======''',''' 
 +---+
 |   |
 |   0
 |
 |
 |
=======''',''' 
 +---+
 |   |
 |   0
 |   |
 |
 |
=======''',''' 
 +---+
 |   |
 |   0
 |  /|
 |
 |
=======''',''' 
 +---+
 |   |
 |   0
 |  /|\\
 |
 |
=======''','''
 +---+
 |   |
 |   0
 |  /|\\
 |  /
 |
=======''',''' 
 +---+
 |   |
 |   0
 |  /|\\
 |  / \\
 |
======='''] 

#list of different words
words = '''coffee clock pencil cloud moon water computer python hammer chair
window cords musical zebra dog home teacher website frog gamer book guitar
national forest'''.split()


#gets a random word from the list
def getRandomWord(words):
    wordIndex = randint(0, len(words) - 1)
    return words[wordIndex]

def displayBoard(hangmanPics, missedLetters, correctLetters, secretWord):
    print hangmanPics[len(missedLetters)]
    print "Missed Letters:"
    #prints missed letters
    for letter in missedLetters:
        print letter

    blanks = '_'
    #prints the letter if it's correct or blank if it is not
    for i in range(len(secretWord)):
        if(secretWord[i] in correctLetters):
            print secretWord[i],
        else:
            print blanks,
#gets a single letter from the user 
def getGuess(alreadyGuessed):
    while True:
        guess = raw_input("guess a letter: ")
        if(len(guess) != 1):
            print "you can only guess one letter at a time"	
        elif(guess in alreadyGuessed):
            print "You already guessed that letter"
        elif(guess not in 'abcdefghijklmnopqrstuvwxyz'):
            print "You must guess a letter"
        else:
            return guess

#Asks if the user wants to play again
def playAgain():
    print "Do you want to play again? (y/n)"
    return raw_input().lower()


missedLetters = ''
correctLetters = ''
#assigns a random word to secretWord
secretWord = getRandomWord(words)
#specifies amount of tries
tries = 6
gameIsDone = False

#runs the game while true
while True:
    #prints the board
    displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)

    #gets a guess from the user
    guess = getGuess(missedLetters + correctLetters)

    #Adds users guess to correctLetters if it is in the word
    if(guess in secretWord):
        correctLetters = correctLetters + guess

        foundAllLetters = True
        #checks if all letters are correct
        for i in range(len(secretWord)):
            if(secretWord[i] not in correctLetters):
                foundAllLetters = False
                break
        #if all letters are correct, you win
        if foundAllLetters:
            displayBoard(hangmanPics, missedLetters, correctLetters,
                    secretWord)
            print "You Win! The word was %s" % (secretWord)
            gameIsDone = True
    #if users guess is wrong, user loses a try and adds to missedLetters
    else:
        missedLetters = missedLetters + guess
        tries -= 1
        #if the user has no more tries, the game ends
        if(tries <= 0):
            displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)
            print "You have run out of guesses!"
            print "the correct word was %s" % (secretWord)
            gameIsDone = True

    #if the game is done, it will ask user to play again and resets the game
    if(gameIsDone == True):
        if(playAgain() == "y"):
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            tries = 6
            gameIsDone = False
        else:
            break
