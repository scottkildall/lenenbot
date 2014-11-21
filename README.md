lenenbot
========

**@lenenbot** is a Twitterbot that mashes up John Lennon and Vladimir Lenin quotes. It will combine The first half of Lennon/Lenin with the second half of the other to create odd, relevant and funny Tweets.

@lenenbot lives at [https://twitter.com/lenenbot](https://twitter.com/lenenbot)

This is running off a Raspberry PI and uses the Twython library to send Twitter messages.

If you want to make a similar mashup, you can rename the input files used in the Python script as well as the Python script itself.

You will also have to make your own bot's own Twitter account, email and registered Twitter applicaiton, which you can register through Twitter. This will give you consumer and access tokens that you can put in the Python script. 

**Files:**

lenenbot.py: the executable that sends Tweets 

lenin_start.txt: the 1st half of a sentence from Vladimir Lenin

lennon_start.txt: the 1st half of a sentence from John Lennon

lenin_end.txt: the 2nd half of a sentence from Vladimir Lenin

lennon_end.txt: the 2nd half of a sentence from John Lennon

by Scott Kildall  
[www.kildall.com](http://www.kildall.com)



