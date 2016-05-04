from random import randint

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
words = '''coffee clock pencil cloud moon water computer python hammer chair
window cords musical zebra dog home teacher website frog gamer book guitar
national forest'''.split()


def getRandomWord(words):
    wordIndex = randint(0, len(words) - 1)
    return words[wordIndex]

def displayBoard(hangmanPics, missedLetters, correctLetters, secretWord):
    print hangmanPics[len(missedLetters)]
    print "Missed Letters:"
    for letter in missedLetters:
        print letter

    blanks = '_'
    for i in range(len(secretWord)):
        if(secretWord[i] in correctLetters):
            print secretWord[i],
        else:
            print blanks,
    
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

def playAgain():
    print "Do you want to play again? (y/n)"
    return raw_input().lower()


missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
tries = 6
gameIsDone = False

while True:
    displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if(guess in secretWord):
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if(secretWord[i] not in correctLetters):
                foundAllLetters = False
                break
        if foundAllLetters:
            displayBoard(hangmanPics, missedLetters, correctLetters,
                    secretWord)
            print "You Win! The word was %s" % (secretWord)
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        tries -= 1
        if(tries <= 0):
            displayBoard(hangmanPics, missedLetters, correctLetters, secretWord)
            print "You have run out of guesses!"
            print "the correct word was %s" % (secretWord)
            gameIsDone = True

    if(gameIsDone == True):
        if(playAgain() == "y"):
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            tries = 6
            gameIsDone = False
        else:
            break
