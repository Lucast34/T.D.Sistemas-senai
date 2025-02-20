void setup() {
  // put your setup code here, to run once:
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
}

void loop() {
  // put your main code hs, to run repeatedly:
  for (int i = 0; i < 255; ++i){
    digitalWrite(4, HIGH);
    delay(50);
    digitalWrite(4, LOW);
    delay(50);
  }
  delay(50);
}
  /*for (int i = 0; i < 255; ++i){
    digitalWrite(5, HIGH);
    delay(50);
    digitalWrite(5, LOW);
    delay(50);
  }

*/