
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
    buffer2[33] = 9;
    buffer2[34] = '\n';

   buffer2[75] = 3;
    buffer2[76] = 5;
    buffer2[77] = TPS>>8; // de 0 a 1000, 10bits
    buffer2[78] = TPS;
    buffer2[79] = OILP>>8;
    buffer2[80] = OILP;
    buffer2[81] = FUELP>>8;
    buffer2[82] = FUELP;
    buffer2[83] = VAZBICOS>>8;
    buffer2[84] = VAZBICOS;
    buffer2[85] = PoSus_DE>>8;
    buffer2[86] = PoSus_DE;
    buffer2[87] = PoSus_DD>>8;
    buffer2[88] = PoSus_DD;
    buffer2[89] = PoSus_TE>>8;
    buffer2[90] = PoSus_TE;
    buffer2[91] = PoSus_TD>>8;
    buffer2[92] = PoSus_TD;
    buffer2[93] = PosVolante>>8;
    buffer2[94] = PosVolante;
    buffer2[95] = BatCor>>8;
    buffer2[96] = BatCor;
    buffer2[97] = VentCor>>8;
    buffer2[98] = VentCor;
    buffer2[99] = BombCor>>8;
    buffer2[100] = BombCor;
    buffer2[101]= PresFreio_D>>8;
    buffer2[102] = PresFreio_D;
    buffer2[103]= PresFreio_T>>8;
    buffer2[104] = PresFreio_T;
    buffer2[105] = TIMERCOUNT>>8;
    buffer2[106] = TIMERCOUNT;
    buffer2[107] = 9;
    buffer2[108] = '\n';

    buffer3[109] = 4;
    buffer3[110] = BAT>>8; //max1500
    buffer3[111] = BAT;
    buffer3[112] = ECT>>8;
    buffer3[113] = ECT;
    buffer3[114] = OILT>>8;
    buffer3[115] = OILT;
    buffer3[116] = Tempdisco_DE>>8;
    buffer3[117] = Tempdisco_DE;
    buffer3[118] = Tempdisco_DD>>8;
    buffer3[119] = Tempdisco_DD;
    buffer3[120] = Tempdisco_TE>>8;
    buffer3[121] = Tempdisco_TE;
    buffer3[122] = Tempdisco_TD>>8;
    buffer3[123] = Tempdisco_TD;
    buffer3[124] = TempVentoinha>>8;
    buffer3[125] = TempVentoinha;
    buffer3[126] = TempBomba>>8;
    buffer3[127] = TempBomba;
    buffer3[128] = PosRunners>>8;
    buffer3[129] = PosRunners;
    buffer3[130] = (AcioVent>>8) | (AcioBomba<<7) | (AcioMata<<5);
    buffer3[131] = GPS_Lat>>16;
    buffer3[132] = GPS_Lat>>8;
    buffer3[133] = GPS_Lat;
    buffer3[134] = GPS_Long>>16;
    buffer3[135] = GPS_Long>>8;
    buffer3[136] = GPS_Long;
    buffer3[137] = GPS_NS;
    buffer3[138] = GPS_EW;
    buffer3[139] = hgps.hour;
    buffer3[140] = hgps.minute;
    buffer3[141] = hgps.seconds;
    buffer3[142] = hgps.milliseconds;
    buffer3[143] = hgps.year;
    buffer3[144] = hgps.month;
    buffer3[145] = hgps.day;
    buffer3[146] = TIMERCOUNT>>8;
    buffer3[147] = TIMERCOUNT;
    buffer3[148] = 9;
    buffer3[149] = '\n';

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
