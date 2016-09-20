from random import randint
import sys

num = randint(1,100)

def guess(tries, number):
	tries += 1
	unum = int(raw_input())
	if(unum > number):
		print "Your number is too big"
		guess(tries, number)
	elif(unum < number):
		print "Your number it too small"
		guess(tries, number)
	elif(unum == number):
		print "You guessed the correct number!"
		print "You used %i tries" % (tries)
		end()
	else:
		print "Something went wrong"
		guess(tries)

def end():
	print "Do you want to play again? (y/n)"
	reply = raw_input()
	if(reply.lower() == "y"):
		print "Guess a number between 1 and 100"
		guess(0, randint(1,100))
	elif(reply.lower() == "n"):
		sys.exit
	else:
		print "something went wrong"
		end()

print "Guess a number between 1 and 100"
guess(0, num)

