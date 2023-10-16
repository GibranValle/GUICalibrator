void serialMenu2() {
  if (serialIncome) {
    while (mySerial.available()) {
      char inChar = (char)mySerial.read();
      inputString2 += inChar;
      if (inChar == '\n') stringComplete2 = true;
      serialIncome = false;
    }
  }

  // stall if not complete
  if (!stringComplete2) return;

  // save local string an clean buffer and flag
  char fisrtLetter2 = inputString2[0];
  stringComplete2 = false;
  inputString2 = "";

  switch (fisrtLetter2) {
    case 'S':
      performShortExposure();
      Serial.println("S");
      mySerial.println("S");
      break;

    case 'L':
      performLongxposure();
      Serial.println("L");
      mySerial.println("L");
      break;

    case 'X':
      endExposure();
      Serial.println("X");
      mySerial.println("X");
      TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
      break;

    case 'T':
      TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
      Serial.println("T");
      mySerial.println("T");
      break;
  }
}