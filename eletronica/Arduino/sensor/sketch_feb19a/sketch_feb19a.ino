const int led = 8;    // LED positivo conectado ao pino digital 9
const int sensor = 7; // Pino de sinal do sensor PIR conectado ao pino digital 5

void setup() {
  pinMode(led, OUTPUT);  // Configura o LED como saída
  pinMode(sensor, INPUT); // Configura o sensor PIR como entrada
  Serial.begin(9600);
}
void loop() {
  int movimento = 0; // Lê o estado do sensor PIR
  movimento =  digitalRead(sensor);

  if (movimento == HIGH) {
    digitalWrite(led, HIGH);  // Acende o LED quando o movimento for detectado
    Serial.println("MOVIMENTO");
  } else {
    digitalWrite(led, LOW);   // Apaga o LED quando não houver movimento
    Serial.println("SEM MOVIMENTO");
  }
  delay(140);
}
