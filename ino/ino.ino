
byte buf[16];
byte buf2[22];
byte buf3[16];
byte buf4[30];
int a, b, c;
 int i = 0;
  int j = 255;
int k = 0, aux ;


int AX=0;
int AY=0;
int AZ=0;
int SPEEDFRONT=0;
int SPEEDREAR=0;
int SPARK=0;
int SUSP=0;
int TIME=0;
int OILP=0;
int FUELP=0;
int TPS=0;
int PFREIOT=0;
int PFREIOD=0;
int POSVOL=0;
int ECT=0;
int BAT=0;
int BOMBA=0;
int VENT=0;
 int TEMPPDU=0;
int TEMPBREAK1=0;
int TEMPBREAK2=0;

int32_t ext1_DE=0;
int32_t ext2_DE=0;
int32_t ext3_DE=0;
int32_t ext1_DD=0;
int32_t ext2_DD=0;
int32_t ext3_DD=0;
int32_t ext1_TE=0;
int32_t ext2_TE=0;

void setup() {

    
   Serial.begin(115200);
   delay(100);
   updateBuffer();
}

void loop()
{
 a = analogRead(A0);
 b = analogRead(A1);
 c = analogRead(A3);

 AX = i*250;
 AY = j*250;
 AZ = i*250;

 aux = 200*i;
 OILP = aux;

 aux = 5*i;
 ECT = aux;

 aux = 3*i;
 FUELP= aux;

 aux = i*65790;
 ext2_DD = aux;
 

 if( i == 255 ){
   i = 0;
 }
 i++;
 if( j == 255 ){
    j = 0;
 }
 j++;
updateBuffer();
Serial.write(buf, 16);
if (TIME%2 == 0){
  Serial.write(buf2, 22);
  //Serial.write(buf4, 30);
}
if(TIME%20 == 0){
  Serial.write(buf3, 16);
 }
TIME++;
delay(20);
}

void updateBuffer(){
  buf[0] = 1;
   buf[1] = 5;
   buf[2] = AX >> 8;
   buf[3] = AX;
   buf[4] = AY >> 8;
   buf[5] = AY;
   buf[6] = AZ >> 8;
   buf[7] = AZ;
   buf[8] = SPEEDFRONT;
   buf[9] = SPEEDREAR;
   buf[10] = (SPARK << 7)|SUSP>>8;
   buf[11] = SUSP;
   buf[12] = TIME>>8;
   buf[13] = TIME;
   buf[14] = 9;
   buf[15] = 10;

   buf2[0] = 2;
   buf2[1] = 5;
   buf2[2] = OILP>>8;
   buf2[3] = OILP;
   buf2[4] = FUELP>>8;
   buf2[5] = FUELP;
   buf2[6] = TPS>>8;
   buf2[7] = TPS;
   buf2[8] = PFREIOT>>8;
   buf2[9] = PFREIOT;
   buf2[10] = PFREIOD>>8;
   buf2[11] = PFREIOD;
   buf2[12] = POSVOL>>8;
   buf2[13] = POSVOL;
   buf2[14] = 0;
   buf2[15] = 0;
   buf2[16] = 0;
   buf2[17] = 0;
   buf2[18] = TIME>>8;
   buf2[19] = TIME;
   buf2[20] = 9;
   buf2[21] = 10;

   buf3[0] = 3;
   buf3[1] = 5;
   buf3[2] = ECT>>8;
   buf3[3] = ECT;
   buf3[4] = BAT>>8;
   buf3[5] = BAT;
   buf3[6] = TEMPPDU>>8 | BOMBA<<7 | VENT<<5;
   buf3[7] = TEMPPDU;
   buf3[8] = TEMPBREAK1>>8;
   buf3[9] = TEMPBREAK1;
   buf3[10] = TEMPBREAK2>>8;
   buf3[11] = TEMPBREAK2;
   buf3[12] = TIME>>8;
   buf3[13] = TIME;
   buf3[14] = 9;
   buf3[15] = 10;

    buf4[0] = 4;
    buf4[1] = 5;
    buf4[2] = ext1_DE >> 16;
    buf4[3] = ext1_DE >> 8;
    buf4[4] = ext1_DE;
    buf4[5] = ext2_DE >> 16;
    buf4[6] = ext2_DE >> 8;
    buf4[7] = ext2_DE;
    buf4[8] = ext3_DE >> 16;
    buf4[9] = ext3_DE >> 8;
    buf4[10] = ext3_DE;
    buf4[11] = ext1_DD >> 16;
    buf4[12] = ext1_DD >> 8;
    buf4[13] = ext1_DD;
    buf4[14] = ext2_DD >> 16;
    buf4[15] = ext2_DD >> 8;
    buf4[16] = ext2_DD;
    buf4[17] = ext3_DD >> 16;
    buf4[18] = ext3_DD >> 8;
    buf4[19] = ext3_DD;
    buf4[20] = ext1_TE >> 16;
    buf4[21] = ext1_TE >> 8;
    buf4[22] = ext1_TE;
    buf4[23] = ext2_TE >> 16;
    buf4[24] = ext2_TE >> 8;
    buf4[25] = ext2_TE;
    buf4[26] = TIME>>8;
    buf4[27] = TIME; 
    buf4[28] = 9;
    buf4[29] = 10;  
}
