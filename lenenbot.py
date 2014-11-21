#! /user/bin/env python
import sys
import datetime
import random

from twython import Twython

import random

import tweeter as Tweeter

# main entry, gets called by cron, chooses a 1/125 possbility for Tweeting
# this is based on cron starting at 6am (PST) - 9pm (PST), 15 hours total
# every 9 minutes is about 1 out of every 100 for an average of 1 tweet/day
def Activate():
	randChance = 1.0/100.0
	
	randomNum = random.random()

	# this outputs to cronlog, so we can tell if script is working, use randomNum to switch up output
	outStr = "Activate (lenenbot.py)\n"
	outStr = outStr + "randomNum = " + str(randomNum) + "\n"
	outStr = outStr + "randomChance " + str(randChance) + "\n"

	# if we are in random range, choose a random quotebot and tweet it
	if randChance >= randomNum:
		tweetedMsg = tweetComboQuote()
		outStr = outStr + "TWEETING\n"
		outStr = outStr + tweetedMsg
	else:
		outStr = outStr + "NO TWEET SENT"

	print outStr

def tweetComboQuote():
	tweetStr = generateTweet()
	Tweeter.tweetMessage(Tweeter.getKeys("keys.txt"), tweetStr)
	saveTweet(tweetStr)
	return tweetStr

def generateTweet():
	# arrays of half sections of each quote
	johnstart = getFileLines("lennon_start.txt")
	johnend = getFileLines("lennon_end.txt")
	vladstart = getFileLines("lenin_start.txt")
	vladend = getFileLines("lenin_end.txt")

	# create new tweet
	if random.randint(1, 2) == 1:
        	# John Lennon start, Vlad Lenin end
        	tweet = johnstart[random.randint(0,len(johnstart)-1)].rstrip()
        	tweet += " "
        	tweet += vladend[random.randint(0,len(vladend)-1)]
	else:
        	# Vlad Lenin start, John Lenin end
        	tweet = vladstart[random.randint(0,len(vladstart)-1)].rstrip()
        	tweet += " "
        	tweet += johnend[random.randint(0,len(johnend)-1)]

	return tweet

# makes an array from lines in a file, stripping off the newlines
def getFileLines(filename):
	f = open( filename, "r" )
	arr = []
	for line in f:
    		arr.append( line.rstrip('\n') )
	f.close()
	return arr

def saveTweet(tweet):	
	# save all transmitted tweets, just for sake of recording
	f = open("senttweets.txt", "a")
	f.write(tweet)
	f.write("\n")
	f.close()

if __name__ == "__main__":
	Activate()
