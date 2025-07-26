//#include <SoftwareSerial.h>
#include <String.h>
#include <LiquidCrystal.h>
LiquidCrystal lcd(4, 5, 6, 7, 8, 9);
String str;
//SoftwareSerial mySerial(2, 3); 

const int TURBINE1=A0;
const int TURBINE2=A1;
const int SOLAR=A2;
const int WATERTANK_BOT=A3;
const int WATERTANK_TOP=A4;
const int MOTOR=10;

const int AI_RELAY=11;

float TURBINE1_VALUE=0;
float TURBINE2_VALUE=0;
float SOLAR_VALUE=0;


int TURBINE1_VAL=0;
int TURBINE2_VAL=0;
int SOLAR_VAL=0;



void setup()
{
  Serial.begin(9600);                 // the GPRS baud rate 
//  mySerial.begin(9600);
  pinMode(TURBINE1, INPUT); 
  pinMode(TURBINE2, INPUT);
  pinMode(SOLAR, INPUT);
  pinMode(WATERTANK_BOT, INPUT);
  pinMode(WATERTANK_TOP, INPUT);
  pinMode(MOTOR, OUTPUT);
  pinMode(AI_RELAY, OUTPUT);
   digitalWrite(MOTOR,LOW);
    digitalWrite(AI_RELAY,LOW);
      lcd.begin(16, 2);
       lcd.setCursor(0, 0);
      lcd.print("IOT BASED HYBRID");
      lcd.setCursor(0, 1);
      lcd.print(" PWR GENERATION "); 
      delay(2000); 
      lcd.setCursor(0, 0);
      lcd.print(" BOOTING MODEM  ");
      lcd.setCursor(0, 1);
      lcd.print(" PLEASE WAIT . ."); 
      delay(2000); 
      lcd.setCursor(0, 0);
      lcd.print("  MODEM READY!  ");
      lcd.setCursor(0, 1);
      lcd.print("                "); 
      delay(2000);
      
} 
void loop()
{       
         TURBINE1_VALUE=  analogRead(TURBINE1);
         TURBINE1_VALUE*=15;
         TURBINE1_VALUE/=1023;
         TURBINE1_VAL=TURBINE1_VALUE;
         
         TURBINE2_VALUE=  analogRead(TURBINE2);
         TURBINE2_VALUE*=15;
         TURBINE2_VALUE/=1023;
         TURBINE2_VAL=TURBINE2_VALUE;
         
         SOLAR_VALUE=  analogRead(SOLAR);
         SOLAR_VALUE*=12;
         SOLAR_VALUE/=1023;
         SOLAR_VAL=SOLAR_VALUE;
       
      if(TURBINE1_VALUE>SOLAR_VALUE)
      {
          digitalWrite(AI_RELAY,HIGH);
      }
      else if(TURBINE2_VALUE>SOLAR_VALUE)
      {
          digitalWrite(AI_RELAY,HIGH);
      }
      else 
      {
          digitalWrite(AI_RELAY,LOW);
      }
      
      lcd.setCursor(0, 0);
      lcd.print("TUR1:");
      lcd.print(TURBINE1_VAL);
      lcd.print("V ");
      lcd.print("TUR2:");
      lcd.print(TURBINE2_VAL);
      lcd.print("V ");
      lcd.setCursor(0, 1);
      lcd.print("SOLR:");
      lcd.print(SOLAR_VAL);
      lcd.print("V");

      if(digitalRead(WATERTANK_BOT)==LOW&&digitalRead(WATERTANK_TOP)==LOW)
      {
        lcd.print("TANK:0%");
        digitalWrite(MOTOR,HIGH);
      }
      if(digitalRead(WATERTANK_BOT)==HIGH&&digitalRead(WATERTANK_TOP)==LOW)
      {
        lcd.print("TANK:50%");
      }
      
      if(digitalRead(WATERTANK_BOT)==HIGH&&digitalRead(WATERTANK_TOP)==HIGH)
      {
        lcd.print("TANK:100%");
        digitalWrite(MOTOR,LOW);
      }



      
   

     pingserver();
     delay(1000);
}
 



void pingserver()
{

   
      Serial.print("TURBINE INLET:");
      Serial.print(TURBINE1_VAL);
      Serial.print("V   ");
      Serial.print("TURBINE OUTLET:");
      Serial.print(TURBINE2_VAL);
      Serial.print("V   ");
      Serial.print("SOLAR:");
      Serial.print(SOLAR_VAL);
      Serial.println("V");

      
  /*
ShowSerialData();
  Serial.println("AT");
  delay(1000);
   ShowSerialData();        
        
  Serial.println("AT+CPIN?");
  delay(1000);
   ShowSerialData();     
         
  Serial.println("AT+CREG?");
  delay(1000);
ShowSerialData();
            
        
  Serial.println("AT+CGATT?");
  delay(1000);
ShowSerialData();
               
        
  Serial.println("AT+CIPSHUT");
  delay(1000);
ShowSerialData();
             
        
  Serial.println("AT+CIPSTATUS");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
            
        
  Serial.println("AT+CIPMUX=0");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

        
         
  Serial.println("AT+CSTT=\"airtelgprs.com\"");//start task and setting the APN,
  delay(1000);
  ShowSerialData();
 
          
         
  Serial.println("AT+CIICR");//bring up wireless connection
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
           
        
  Serial.println("AT+CIFSR");//get local IP adress
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
             
         
  Serial.println("AT+CIPSPRT=0");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

            
        
  Serial.println("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
         
       
  Serial.println("AT+CIPSEND");//begin send data to remote server
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
  
        
        
  str="GET http://api.thingspeak.com/update?api_key=GBOBL7YAJVG2CCR9&field1=" + String(TURBINE1_VAL);
  Serial.println(str);//begin send data to remote server
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

          
         
  Serial.println((char)26);//sending
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
//waitting for reply, important! the time is base on the condition of internet 
  Serial.println();
  ShowSerialData();
 
          
         
  Serial.println("AT+CIPSHUT");//close the connection
  delay(100);
  ShowSerialData();  
           
        
  
 
ShowSerialData();
  Serial.println("AT");
  delay(1000);
   ShowSerialData();        
        
  Serial.println("AT+CPIN?");
  delay(1000);
   ShowSerialData();     
         
  Serial.println("AT+CREG?");
  delay(1000);
ShowSerialData();
            
        
  Serial.println("AT+CGATT?");
  delay(1000);
ShowSerialData();
               
        
  Serial.println("AT+CIPSHUT");
  delay(1000);
ShowSerialData();
             
        
  Serial.println("AT+CIPSTATUS");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
            
        
  Serial.println("AT+CIPMUX=0");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

        
         
  Serial.println("AT+CSTT=\"airtelgprs.com\"");//start task and setting the APN,
  delay(1000);
  ShowSerialData();
 
          
         
  Serial.println("AT+CIICR");//bring up wireless connection
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
           
        
  Serial.println("AT+CIFSR");//get local IP adress
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
             
         
  Serial.println("AT+CIPSPRT=0");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

            
        
  Serial.println("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
         
       
  Serial.println("AT+CIPSEND");//begin send data to remote server
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
  
        
        
  str="GET http://api.thingspeak.com/update?api_key=GBOBL7YAJVG2CCR9&field2=" + String(TURBINE2_VAL);
  Serial.println(str);//begin send data to remote server
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

          
         
  Serial.println((char)26);//sending
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
//waitting for reply, important! the time is base on the condition of internet 
  Serial.println();
  ShowSerialData();
 
          
         
  Serial.println("AT+CIPSHUT");//close the connection
  delay(100);
  ShowSerialData();  
          
  
     
ShowSerialData();
  Serial.println("AT");
  delay(1000);
   ShowSerialData();        
        
  Serial.println("AT+CPIN?");
  delay(1000);
   ShowSerialData();     
         
  Serial.println("AT+CREG?");
  delay(1000);
ShowSerialData();
            
        
  Serial.println("AT+CGATT?");
  delay(1000);
ShowSerialData();
               
        
  Serial.println("AT+CIPSHUT");
  delay(1000);
ShowSerialData();
             
        
  Serial.println("AT+CIPSTATUS");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
            
        
  Serial.println("AT+CIPMUX=0");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

        
         
  Serial.println("AT+CSTT=\"airtelgprs.com\"");//start task and setting the APN,
  delay(1000);
  ShowSerialData();
 
          
         
  Serial.println("AT+CIICR");//bring up wireless connection
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
           
        
  Serial.println("AT+CIFSR");//get local IP adress
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
             
         
  Serial.println("AT+CIPSPRT=0");
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

            
        
  Serial.println("AT+CIPSTART=\"TCP\",\"api.thingspeak.com\",\"80\"");//start up the connection
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
 
         
       
  Serial.println("AT+CIPSEND");//begin send data to remote server
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
  
        
        
  str="GET http://api.thingspeak.com/update?api_key=GBOBL7YAJVG2CCR9&field3=" + String(SOLAR_VAL);
  Serial.println(str);//begin send data to remote server
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();

          
         
  Serial.println((char)26);//sending
  delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
delay(1000);
ShowSerialData();
//waitting for reply, important! the time is base on the condition of internet 
  Serial.println();
  ShowSerialData();
 
          
         
  Serial.println("AT+CIPSHUT");//close the connection
  delay(100);
  ShowSerialData();  
  */
  
     
} 
void ShowSerialData()
{  
          
          TURBINE1_VALUE=  analogRead(TURBINE1);
         TURBINE1_VALUE*=15;
         TURBINE1_VALUE/=1023;
         TURBINE1_VAL=TURBINE1_VALUE;
         
         TURBINE2_VALUE=  analogRead(TURBINE2);
         TURBINE2_VALUE*=15;
         TURBINE2_VALUE/=1023;
         TURBINE2_VAL=TURBINE2_VALUE;
         
         SOLAR_VALUE=  analogRead(SOLAR);
         SOLAR_VALUE*=12;
         SOLAR_VALUE/=1023;
         SOLAR_VAL=SOLAR_VALUE;
       
      
      lcd.setCursor(0, 0);
      lcd.print("TUR1:");
      lcd.print(TURBINE1_VAL);
      lcd.print("V ");
      lcd.print("TUR2:");
      lcd.print(TURBINE2_VAL);
      lcd.print("V ");
      lcd.setCursor(0, 1);
      lcd.print("SOLR:");
      lcd.print(SOLAR_VAL);
      lcd.print("V");
 if(TURBINE1_VALUE>SOLAR_VALUE)
      {
          digitalWrite(AI_RELAY,HIGH);
      }
      else if(TURBINE2_VALUE>SOLAR_VALUE)
      {
          digitalWrite(AI_RELAY,HIGH);
      }
      else 
      {
          digitalWrite(AI_RELAY,LOW);
      }
      if(digitalRead(WATERTANK_BOT)==LOW&&digitalRead(WATERTANK_TOP)==LOW)
      {
        lcd.print("TANK:0%");
        digitalWrite(MOTOR,HIGH);
      }
      if(digitalRead(WATERTANK_BOT)==HIGH&&digitalRead(WATERTANK_TOP)==LOW)
      {
        lcd.print("TANK:50%");
      }
      
      if(digitalRead(WATERTANK_BOT)==HIGH&&digitalRead(WATERTANK_TOP)==HIGH)
      {
        lcd.print("TANK:100%");
        digitalWrite(MOTOR,LOW);
      }
}
