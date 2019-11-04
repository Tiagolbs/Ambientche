int a=0;
void setup() { //inicializacao da COM serial e dos pinos dos LEDs
  Serial.begin(9600);
  for(int i=2;i<=8;i++){
    pinMode(i,OUTPUT);
    digitalWrite(i,LOW);
  }
}
 
void loop() {
  if (Serial.available()){ //lê a entrada serial e converte char->int
    a=Serial.read();
    a-=48;
  }
  if(a<=8 and a>=2){ //liga o LED indicado se este estiver desligado e vice-versa
    Serial.print("Pino ");
    Serial.print(a);
    if(digitalRead(a)){
      digitalWrite(a,LOW);
      Serial.println("foi desligado!");
    }else{
      digitalWrite(a,HIGH);
      Serial.println("foi ligado!");
    }
  }
  delay(100);
}
