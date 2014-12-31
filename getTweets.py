'''
Twitter Mood Box 
inspired by The Worlds Mood in a box: 
	http://www.instructables.com/id/Twitter-Mood-Light-The-Worlds-Mood-in-a-Box/

Using Twitter Streaming API to get a sample of tweets
Process Tweets to find the top emotion
Communicate top emotion via serial to Arduino

by Judy Stephen
Created: December 26, 2014
Updated: December 30, 2014
'''

import time
import json
import tweepy
import serial
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob.classifiers import NaiveBayesClassifier

consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

#Connect to Arduino
ser = serial.Serial("COM7")
print "Serial name is: " + ser.name
#allow Arduino to setup
time.sleep(2)
ser.write('0')

dataFile = 'data.txt'


class Listener(StreamListener):
	"""An instance of StreamListener"""
	numberOfTweets = 0

	def on_data(self, data):
		"""Saves up to 500 tweets in dataFile """
		if self.numberOfTweets < 50:
			tweet = (data.split(',"text":')[1]).split(',"source"')[0] 
			with open(dataFile, 'a') as f:
				f.write(tweet + '\n')
			self.numberOfTweets = self.numberOfTweets + 1
		else:
			return False

	def on_error(self, status):
		print status


def connectStream():
	"""Connect to stream endpoint"""
	twitterStream = Stream(auth, Listener())
	twitterStream.sample(languages=['en'])


def getTopEmotion():
	"""Return the most popular emotion on Twitter"""
	#Classify each tweet in the dataFile 
	emotions = []
	tweetData = open(dataFile, 'r')
	for line in tweetData:
		emotions.append(cl.classify(line))
	tweetData.close()

	#empty dataFile
	open(dataFile, 'w').close()

	numHappy = emotions.count('happy')
	numSad = emotions.count('sad')
	numSurprise = emotions.count('surprise')
	numAngry = emotions.count('anger')
	topEmotion = max(numSad, numHappy, numSurprise, numAngry)
	print "Top emotion count is " + str(topEmotion)

	if(topEmotion == numHappy):
		return "Happy"
	elif(topEmotion == numSad):
		return "Sad"
	elif(topEmotion == numSurprise):
		return "Surprise"
	elif(topEmotion == numAngry):
		return "Anger"


def commSerial(twitterMood):
	""" Communicate the emotions via serial. Emotions 
		represented as integers:
			Happy     1
			Sad       2
			Surprise  3
			Anger     4

		Pre: twitterMood is type string of the above emotions"""

	if twitterMood == "Happy":
		print "Happy"
		ser.write('1')
	elif twitterMood == "Sad":
		print "Sad"
		ser.write('2')
	elif twitterMood == "Surprise":
		print "Surprise"
		ser.write('3')
	elif twitterMood == "Anger":
		print "Anger"
		ser.write('4')

	#delay sometime for light to show
	time.sleep(1)


if __name__ == '__main__':
	#authentication
	try:
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		print 'Successfully authenticated'
	except:
		print 'Failed to authenticate'
	
	#train the classifier
	with open('train.json', 'r') as fp:
		cl = NaiveBayesClassifier(fp, format="json")

	#Main loop
	while True:
		connectStream()
		print "Calculating most common emotion..."
		topMood = getTopEmotion()
		commSerial(topMood)
		time.sleep(10)