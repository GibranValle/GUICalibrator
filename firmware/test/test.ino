// UPDATED FIRMWARE TO MATCH NEW PCB
#include "variables.h"

void setup() {
  // initialize serial:
  Serial.begin(9600);
  relayInit();
  pinMode(ledPin, OUTPUT);
  noInterrupts();
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0;
  OCR1A = 15625;           // 1 sec
  TCCR1B |= (1 << WGM12);  // CTC MODE
  TCCR1B |= (1 << CS12);   // 256 PRESCALE
  TCCR1B |= (1 << CS10);   // 256 PRESCALE
  //TIMSK1 |= (1 << OCIE1A);  //enable timer
  interrupts();
}

void loop() {
  // stall if not complete
  if (!stringComplete) return;

  // save local string an clean buffer and flag
  char fisrtLetter = inputString[0];
  stringComplete = false;
  inputString = "";
  

  switch (fisrtLetter) {
    case 'M':
      sensorValue = analogRead(analogInPin);
      Serial.print("M:");
      Serial.println(sensorValue);
      break;

    case 'S':
      performShortExposure();
      Serial.println("S");
      break;

    case 'L':
      performLongxposure();
      Serial.println("L");
      break;

    case 'X':
      endExposure();
      Serial.println("X");
      TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
      break;

    case 'T':
      TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
      Serial.println("T");
      break;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') stringComplete = true;
  }
}

ISR(TIMER1_COMPA_vect) {
  countTime++;
  if (countTime > maxTime) {
    Serial.println("E");
    endExposure();
    TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
  }
}
