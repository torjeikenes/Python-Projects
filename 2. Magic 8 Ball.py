from random import randint
import time
import sys

print "Welcome to the magic 8-Ball"

answers = ["Yes", "No", "Maybe", "Don't ask me", "If you are lucky", "Most likely", "Probably not",  "Most sources say no", "Don't count on it"]

def question():
	print "Type a question: "
	question = raw_input()
	print "Thinking..."
	time.sleep(3)
	print answers[randint(1,9)]
	end()

def end():
	print "Thanks you playing! Do you want to play again? (Y/N)"
	reply = raw_input()
	if(reply == "Y"):
		question()
	elif(reply == "N"):
		sys.exit
	else:
		print "I don't know what that means."
		end()

question()
