void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); 
}

void loop() {
  int timeIn = 500;
  int timeContinue = 1;
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(LED_BUILTIN, LOW);
  delay(timeContinue);
  digitalWrite(LED_BUILTIN, HIGH);
  digitalWrite(LED_BUILTIN, LOW);
  delay(timeContinue);
    digitalWrite(LED_BUILTIN, HIGH);
  delay(timeContinue);
  digitalWrite(LED_BUILTIN, LOW);
  delay(timeIn);
}

