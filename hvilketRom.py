from random import randint
import sys

amountOfRooms = 6
tries = 3

def randomRoom():
    room = int(randint(1, amountOfRooms))
    return room


def whatRoom(triesLeft):
    room = randomRoom()
    guess = int(raw_input("guess what room I am in: "))
    if(guess != room):
        if(triesLeft <= 1):
            print "You used all your tries"
            end()
        else:
            print "You guessed the wrong room."
            triesLeft -= 1
            whatRoom(triesLeft)
    elif(guess == room):
        print "Congratulations! You found me"
        end()
    else:
        print "something went wrong"

def end():
    print "Do you want to play again? (y/n)"
    answer = raw_input().lower()
    if(answer == "y"):
        whatRoom(tries)
    elif(answer == "n"):
        sys.exit()
    else:
        print "you didn't type y or n"
        end()


whatRoom(tries)
