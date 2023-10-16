void serialMenu1() {
  // stall if not complete
  if (!stringComplete) return;

  // save local string an clean buffer and flag
  char fisrtLetter = inputString[0];
  stringComplete = false;
  inputString = "";

  switch (fisrtLetter) {
    case 'S':
      performShortExposure();
      Serial.println("S");
      mySerial.println("Short exposure");
      break;

    case 'L':
      performLongxposure();
      Serial.println("L");
      mySerial.println("Long exposure");
      break;

    case 'X':
      endExposure();
      Serial.println("X");
      mySerial.println("End exposure");
      TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
      break;

    case 'T':
      TIMSK1 = !TIMSK1 & (1 << OCIE1A);  //disable timer
      Serial.println("T");
      mySerial.println("Test connection");
      break;
  }
}
