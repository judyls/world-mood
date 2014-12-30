worlds-mood
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
on the Arduino (it is important to show the right colors)

##Additional ideas
It might be wise to play around with the training set at train.json. The accuracy of each mood depends on the quality of the 
training set. If possible try to use a more thorough training set. 

You could also try changing the sleep time in line 
