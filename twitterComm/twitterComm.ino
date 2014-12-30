/*Decide color of LED by numbers read in serial
  Used in conjunction with getTweets.py
  Materials:
    1 5mm Tricolor RGB LED
    3 220 ohm resistors
  By: Judy Stephen
  Created: December 30, 2014
  Updated: December 30, 2014*/
const int redLED = 3;
const int greenLED = 5;
const int blueLED = 6;

void setup()
{
  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(blueLED, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  //have the arduino wait to receive input
  while (Serial.available() == 0);
  
  //Read the input 
  int val = Serial.read() - '0';
  
  if(val == 1){
    //happy LED GREEN
    Serial.println("Happy");
    analogWrite(redLED, 0);
    analogWrite(greenLED, 50);
    analogWrite(blueLED, 0);
  } else if (val == 2){
    //sad LED BLUE
    Serial.println("Sad");
    analogWrite(redLED, 0);
    analogWrite(greenLED, 0);
    analogWrite(blueLED, 50);
  } else if(val == 3) {
    //surprise LED ORANGE
    Serial.println("Surprise");
    analogWrite(greenLED, 7);\
    analogWrite(blueLED, 0);
    analogWrite(redLED, 200);
  } else if(val == 4) {
    //anger LED RED
    Serial.println("Anger");
    analogWrite(greenLED, 0);\
    analogWrite(blueLED, 0);
    analogWrite(redLED, 50);
  } else {
    Serial.println("Unknown command");
    analogWrite(redLED, 0);
    analogWrite(greenLED, 0);
    analogWrite(blueLED, 0);
  }
}
