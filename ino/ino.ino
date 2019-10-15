
byte buf[16];
byte buf2[22];
byte buf3[14];
int a, b, c;
 int i = 0;
  int j = 255;
int k = 0, aux ;


void setup() {

    
   Serial.begin(115200);
   delay(100);
       buf[0] = 1;
   buf[1] = 5;
   buf[8] = 100;
   buf[9] = 85;
   buf[10] = 1 << 7;
   buf[11] = 0;
   buf[12] = 0;
   buf[13] = 0;
   buf[14] = 9;
   buf[15] = 10;

   buf2[0] = 2;
   buf2[1] = 5;
   buf2[8] = 100;
   buf2[9] = 85;
   buf2[10] = 1 << 7;
   buf2[11] = 0;
   buf2[12] = 0;
   buf2[13] = 0;
   buf2[14] = 9;
   buf2[15] = 0;
   buf2[16] = 0;
   buf2[17] = 0;
   buf2[18] = 0;
   buf2[19] = 0;
   buf2[20] = 9;
   buf2[21] = 10;


}

void loop()
{
 a = analogRead(A0);
 b = analogRead(A1);
 c = analogRead(A3);

 buf[2] = i;
 buf[3] = a && 11111111;
 buf[4] = j;
 buf[5] = b && 11111111;
 buf[6] = c >> 8;
 buf[7] = c && 11111111;
 if (buf[13] == 255){
    buf[12] = buf[12] + 1;
    buf2[18] = buf2[18] + 1;
 } 
 buf[13] = buf[13] + 1;
 buf2[19] = buf2[19] + 1;

 aux = 2*i;
 buf2[2]= aux >> 8;
 buf2[3]= aux;

 aux = 3*i;
 buf2[4]= aux >> 8;
 buf2[5]= aux;

 if( i == 255 ){
   i = 0;
 }
 i++;
 if( j == 255 ){
    j = 0;
 }
 j++;
 
if (k == 1){
  Serial.write(buf2, 22);
  k = -1;
}
k++;
Serial.write(buf, 16);

delay(20);
}
