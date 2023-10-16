// UPDATED FIRMWARE TO MATCH NEW PCB
#include "variables.h"
#include <SoftwareSerial.h>
const byte rxPin = 2;
const byte txPin = 3;
SoftwareSerial mySerial(rxPin, txPin);

void setup() {
  // initialize serial:
  mySerial.begin(9600);
  mySerial.listen();
  attachInterrupt(digitalPinToInterrupt(rxPin), serialEvent2, CHANGE);

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
  serialMenu2();
  serialMenu1();
}

void serialEvent2() {
  if (!serialIncome) {
    serialIncome = true;
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
