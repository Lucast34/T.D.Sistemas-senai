 const int pinoPWM = 9; 
 const int pinoPWM2 = 10; 
 const int pinoPWM3 = 11; 

void myleed(int port);

void setup() {
  pinMode(pinoPWM, OUTPUT); 
  pinMode(pinoPWM2, OUTPUT); 
  pinMode(pinoPWM3, OUTPUT); 
}

void loop(){
  myleed(pinoPWM);
  myleed(pinoPWM2);
  myleed(pinoPWM3);

}

void myleed(int port)
{
    int maximum = 255;
  int minimun = 0;

  analogWrite(pinoPWM,maximum);
  analogWrite(pinoPWM2,maximum);
  analogWrite(pinoPWM3,maximum);

  for (int i = maximum;i > minimun; i--){

    analogWrite(port,i);
    delay(10);
}

  for (int i = 0; i < maximum; i++){
    analogWrite(port,i);
    delay(10);
  }

}