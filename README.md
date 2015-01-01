world-mood
===========

Display the mood of the world from Twitter using the Arduino. 

##Install Modules

Make sure you have installed [tweepy](https://github.com/tweepy/tweepy "Tweepy Doc"), 
[pySerial](http://pyserial.sourceforge.net/pyserial.html "PySerial") and 
[textblob](http://textblob.readthedocs.org/en/dev/ "TextBlob")
The easiest way to install is by using PyPI:

```
pip install tweepy
pip install pyserial
pip install -U textblob
```
##Materials
You will need:

* Arduino (any model will do)
* Tricolor RGB LED
* 3 220 Ohm Resistors
* Wires

##Schematic
Wire the Ardunio as shown in the schematic. Make sure each LED pin is connected to the right pin 
on the Arduino.

![Schematic](https://github.com/judyls/world-mood/blob/master/schematic.png)

##Running 

**Register with Twitter**

Register an app with [Twitter](https://dev.twitter.com/ "Twitter Dev"). Copy and paste your consumer key, consumer secret, access token and access token secret into lines 24-27 in getTweets.py. 

**Build Circuit**

Wire the Arduino according to the schematic (shown above). Upload twitterComm.ino to the Ardunio. Find the serial port your Arduino is using. In getTweets.py change the serial port (line 30) to what your Arduino is using. 

**Using Command Line**

In the command line change to the directory where you downloaded the source code. Now, if you type `python getTweets.py` in the command line you will see the following:

```
Serial name is: COM7
Successfully authenticated
Calculating most common emotion...
Top emotion count is 17
Happy
```

NOTE: your serial name might be different ex. COM12. In addition the emotion count and final emotion might be different. It might take up to 10 seconds for the LED to initially turn on so please be patient. 


##Additional ideas
It might be wise to play around with the training set at train.json. The accuracy of each mood depends on the quality of the 
training set. If possible try to use a more thorough training set. 

You could also try changing the sleep time in line 142 to get faster updates. 

You can add or delete emotions that we can identify. If you do make changes to the number of emotions note that you have to modify both the getTweets.py and twitterComm.ino files.
