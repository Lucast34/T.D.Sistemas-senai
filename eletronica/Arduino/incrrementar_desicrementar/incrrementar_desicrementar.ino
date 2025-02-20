const int pinoPWM = 9; 

void setup() {
  pinMode(pinoPWM, OUTPUT); 
}

void loop() {
  for (int valor = 0; valor <= 255; valor++) {
    analogWrite(pinoPWM, valor);
    delay(10); 
  }

  delay(100);

  for (int valor = 255; valor >= 0; valor--) {
    analogWrite(pinoPWM, valor);
    delay(10);
  }
  delay(100);
}
