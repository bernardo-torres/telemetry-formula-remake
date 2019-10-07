
byte buf[14];
byte buf2[14];
byte buf3[14];
int a, b, c;


void setup() {

   Serial.begin(115200);
   buf[0] = 1;
   buf[1] = 5;
   buf[8] = 100;
   buf[9] = 85;
   buf[10] = 1 << 7;
   buf[11] = 0;
   buf[12] = 0;
   buf[13] = 0;

}

void loop()
{
 a = analogRead(A0);
 b = analogRead(A1);
 c = analogRead(A3);
 buf[2] = a >> 8;
 buf[3] = a && 11111111;
 buf[4] = b >> 8;
 buf[5] = b && 11111111;
 buf[6] = c >> 8;
 buf[7] = c && 11111111;
 if (buf[13] == 255){
    buf[12] = buf[12] + 1;
 } 
 buf[13] = buf[13] + 1;
 
Serial.write(buf, 14);

delay(20);
}
