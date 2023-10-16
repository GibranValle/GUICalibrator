// UPDATED FIRMWARE TO MATCH NEW PCB

// PINS
const int relayOn = 4; // D4
const int ledPin = 5; // D5
//const int relayOff = 2; //D4
const int analogInPin = A2;  // Analog input pin that the potentiometer is attached to

// analog read
int sensorValue = 0;        // value read from the pot

// timer
const int MAX_TIME_SHORT = 20;
const int MAX_TIME_LONG = 600;
int maxTime = 0;
int countTime = 0;

// comunication
String inputString = "";         // a String to hold incoming data
String inputString2 = "";         // a String to hold incoming data

boolean stringComplete = false;  // data arrived
boolean stringComplete2 = false;  // data arrived

boolean serialIncome = false;