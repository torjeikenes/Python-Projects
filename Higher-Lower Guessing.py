from random import randint
import sys

number = randint(1,100)

def guess(tries):
	tries += 1
	unum = int(raw_input())
	if(unum > number):
		print "Your number is too big"
		guess(tries)
	elif(unum < number):
		print "Your number it too small"
		guess(tries)
	elif(unum == number):
		print "You guessed the correct number!"
		print "You used %i tries" % (tries)
	else:
		print "Something went wrong"
		guess(tries)

def end():
	print "Do you want to play again?"
	reply = raw_input()
	if(reply.lower() == "y"):
		guess(0)
	elif(reply.lower() == "n"):
		sys.exit
	else:
		print "something went wrong"
		end()

print "Guess a number between 1 and 100"
guess(0)

