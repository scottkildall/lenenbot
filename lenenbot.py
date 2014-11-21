#! /user/bin/env python
import sys
import datetime
import random

from twython import Twython

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
CONSUMER_KEY = 'roasdkoqwkk8i10kwks09aka'
CONSUMER_SECRET = '4ghmkjal810kdla0wkkoasi'
ACCESS_TOKEN = '1239821-dakos81koamow9918ma0sadsqq'
ACCESS_SECRET = 'saklasooqjdoajfj8f9981mska01mdka09'

# create your Twython object
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET) 

# array of 1st half John Lennon quotes
f = open( "lennon_start.txt", "r" )
johnstart = []
for line in f:
    johnstart.append( line.rstrip('\n') )
f.close()

# array of 2nd half John Lennon quotes                               
f = open( "lennon_end.txt", "r" )
johnend = []
for line in f:
    johnend.append( line.rstrip('\n') )
f.close()

# array of 1st half Vlad Lenin quotes                               
f = open( "lenin_start.txt", "r" )
vladstart = []
for line in f:
    vladstart.append( line.rstrip('\n') )
f.close()

# array of 1st half Vlad Lenin quotes                               
f = open( "lenin_end.txt", "r" )
vladend = []
for line in f:
    vladend.append( line.rstrip('\n') )
f.close()

# create new tweet
if random.randint(1, 2) == 1:
	# John Lennon start, Vlad Lenin end
	nexttweet = johnstart[random.randint(0,len(johnstart)-1)].rstrip()
	nexttweet += " "
	nexttweet += vladend[random.randint(0,len(vladend)-1)]
else:
	# Vlad Lenin start, John Lenin end
	nexttweet = vladstart[random.randint(0,len(vladstart)-1)].rstrip()
	nexttweet += " "
	nexttweet += johnend[random.randint(0,len(johnend)-1)]

# transmit it via Twitter
api.update_status(status=nexttweet)
	
# save all transmitted tweets, just for sake of recording
f = open("senttweets.txt", "a")
f.write(nexttweet)
f.write("\n")
f.close()

# will end up getting saved to screen
print nexttweet

