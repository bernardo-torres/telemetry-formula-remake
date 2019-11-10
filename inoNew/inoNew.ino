
byte buffer1[35];
byte buf2[22];
byte buf3[16];
byte buffer4[30];
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
  Serial.write(buffer4, 30);
}
if(TIME%20 == 0){
  Serial.write(buf3, 16);
 }
TIME++;
delay(20);
}

void updateBuffer(){
    buffer1[0]= 1;
    buffer1[1]= 5;
    buffer1[2]= acelX_DD >> 8;
    buffer1[3]= acelX_DD;
    buffer1[4]= acelY_DD >> 8;
    buffer1[5]= acelY_DD;
    buffer1[6]= acelZ_DD >> 8;
    buffer1[7]= acelZ_DD;
    buffer1[8]= acelX_DE >> 8;
    buffer1[9]= acelX_DE;
    buffer1[10]= acelY_DE >> 8;
    buffer1[11]= acelY_DE;
    buffer1[12]= acelZ_DE >> 8;
    buffer1[13]= acelZ_DE;
    buffer1[14]= acelX_TD >> 8;
    buffer1[15]= acelX_TD;
    buffer1[16]= acelY_TD >> 8;
    buffer1[17]= acelY_TD;
    buffer1[18]= acelZ_TD >> 8;
    buffer1[19]= acelZ_TD;
    buffer1[20]= acelX_TE >> 8;
    buffer1[21]= acelX_TE;
    buffer1[22]= acelY_TE >> 8;
    buffer1[23]= acelY_TE;
    buffer1[24]= acelZ_TE >> 8;
    buffer1[25]= acelZ_TE;
    buffer1[26]= vel_DD;
    buffer_60[27]= vel_DE;
    buffer_60[28]= vel_TD;
    buffer_60[29]= vel_TE;
    buffer_60[30]= RPM>>8;
    buffer_60[31]= RPM;
    buffer_60[32]= Beacon;
    buffer2[33] = TIMERCOUNT>>8;
    buffer2[34] = TIMERCOUNT;
    buffer2[35] = 9;
    buffer2[36] = '\n';

    buffer2[0] = 3;
    buffer2[1] = 5;
    buffer2[2] = TPS>>8; // de 0 a 1000, 10bits
    buffer2[3] = TPS;
    buffer2[4] = OILP>>8;
    buffer2[5] = OILP;
    buffer2[6] = FUELP>>8;
    buffer2[7] = FUELP;
    buffer2[8] = VAZBICOS>>8;
    buffer2[9] = VAZBICOS;
    buffer2[10] = PoSus_DE>>8;
    buffer2[11] = PoSus_DE;
    buffer2[12] = PoSus_DD>>8;
    buffer2[13] = PoSus_DD;
    buffer2[14] = PoSus_TE>>8;
    buffer2[15] = PoSus_TE;
    buffer2[16] = PoSus_TD>>8;
    buffer2[17] = PoSus_TD;
    buffer2[18] = PosVolante>>8;
    buffer2[19] = PosVolante;
    buffer2[20] = BatCor>>8;
    buffer2[21] = BatCor;
    buffer2[22] = VentCor>>8;
    buffer2[23] = VentCor;
    buffer2[24] = BombCor>>8;
    buffer2[25] = BombCor;
    buffer2[26]= PresFreio_D>>8;
    buffer2[27] = PresFreio_D;
    buffer2[28]= PresFreio_T>>8;
    buffer2[29] = PresFreio_T;
    buffer2[30] = TIMERCOUNT>>8;
    buffer2[31] = TIMERCOUNT;
    buffer2[32] = 9;
    buffer2[33] = '\n';

    buffer3[0] = 4;
    buffer3[1] = BAT>>8; //max1500
    buffer3[2] = BAT;
    buffer3[3] = ECT>>8;
    buffer3[4] = ECT;
    buffer3[5] = OILT>>8;
    buffer3[6] = OILT;
    buffer3[7] = Tempdisco_DE>>8;
    buffer3[8] = Tempdisco_DE;
    buffer3[9] = Tempdisco_DD>>8;
    buffer3[10] = Tempdisco_DD;
    buffer3[11] = Tempdisco_TE>>8;
    buffer3[12] = Tempdisco_TE;
    buffer3[13] = Tempdisco_TD>>8;
    buffer3[14] = Tempdisco_TD;
    buffer3[15] = TempVentoinha>>8;
    buffer3[16] = TempVentoinha;
    buffer3[17] = TempBomba>>8;
    buffer3[18] = TempBomba;
    buffer3[19] = PosRunners>>8;
    buffer3[20] = PosRunners;
    buffer3[21] = (AcioVent>>8) | (AcioBomba<<7) | (AcioMata<<5);
    buffer3[22] = GPS_Lat>>16;
    buffer3[23] = GPS_Lat>>8;
    buffer3[24] = GPS_Lat;
    buffer3[25] = GPS_Long>>16;
    buffer3[26] = GPS_Long>>8;
    buffer3[27] = GPS_Long;
    buffer3[28] = GPS_NS;
    buffer3[29] = GPS_EW;
    buffer3[30] = hgps.hour;
    buffer3[31] = hgps.minute;
    buffer3[32] = hgps.seconds;
    buffer3[33] = hgps.milliseconds;
    buffer3[34] = hgps.year;
    buffer3[35] = hgps.month;
    buffer3[36] = hgps.day;
    buffer3[37] = TIMERCOUNT>>8;
    buffer3[38] = TIMERCOUNT;
    buffer3[39] = 9;
    buffer3[40] = '\n';

    buffer4[0] = 4;
    buffer4[1] = 5;
    buffer4[2] = ext1_DE >> 16;
    buffer4[3] = ext1_DE >> 8;
    buffer4[4] = ext1_DE;
    buffer4[5] = ext2_DE >> 16;
    buffer4[6] = ext2_DE >> 8;
    buffer4[7] = ext2_DE;
    buffer4[8] = ext3_DE >> 16;
    buffer4[9] = ext3_DE >> 8;
    buffer4[10] = ext3_DE;
    buffer4[11] = ext1_DD >> 16;
    buffer4[12] = ext1_DD >> 8;
    buffer4[13] = ext1_DD;
    buffer4[14] = ext2_DD >> 16;
    buffer4[15] = ext2_DD >> 8;
    buffer4[16] = ext2_DD;
    buffer4[17] = ext3_DD >> 16;
    buffer4[18] = ext3_DD >> 8;
    buffer4[19] = ext3_DD;
    buffer4[20] = ext1_TE >> 16;
    buffer4[21] = ext1_TE >> 8;
    buffer4[22] = ext1_TE;
    buffer4[23] = ext2_TE >> 16;
    buffer4[24] = ext2_TE >> 8;
    buffer4[25] = ext2_TE;
    buffer4[26] = ext3_TE >> 16;
    buffer4[27] = ext3_TE >> 8;
    buffer4[28] = ext3_TE;
    buffer4[29] = ext1_TD >> 16;
    buffer4[30] = ext1_TD >> 8;
    buffer4[31] = ext1_TD;
    buffer4[32] = ext2_TD >> 16;
    buffer4[33] = ext2_TD >> 8;
    buffer4[34] = ext2_TD;
    buffer4[35] = ext3_TD >> 16;
    buffer4[36] = ext3_TD >> 8;
    buffer4[37] = ext3_TD;
    buffer4[38] = TIME>>8;
    buffer4[39] = TIME; 
    buffer4[40] = 9;
    buffer4[41] = 10;  
}
