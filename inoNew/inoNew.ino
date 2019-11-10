
byte buffer1[37];
byte buffer2[34];
byte buffer3[42];
byte buffer4[42];
int a, b, c;
 int i = 0;
  int j = 255;
int k = 0, aux ;


/*Variaveis globais dos dados*/
uint32_t TIMERCOUNT=0;

/*Flag do Beacon*/
uint8_t BEACON_FLAG = 0;

/*Variáveis do Pacote 1 -> 60Hz*/
uint16_t acelX_DE = 0, //Aceleração no eixo X da placa dianteira esquerda
     acelY_DE = 0, //Aceleração no eixo Y da placa dianteira esquerda
     acelZ_DE = 0, //Aceleração no eixo Z da placa dianteira esquerda
     acelX_DD = 0, //Aceleração no eixo X da placa dianteira direita
     acelY_DD = 0, //Aceleração no eixo Y da placa dianteira direita
     acelZ_DD = 0, //Aceleração no eixo Z da placa dianteira direita
     acelX_TE = 0, //Aceleração no eixo X da placa traseira esquerda
     acelY_TE = 0, //Aceleração no eixo Y da placa traseira esquerda
     acelZ_TE = 0, //Aceleração no eixo Z da placa traseira esquerda
     acelX_TD = 0, //Aceleração no eixo X da placa traseira dianteira
     acelY_TD = 0, //Aceleração no eixo Y da placa traseira dianteira
     acelZ_TD = 0, //Aceleração no eixo Z da placa traseira dianteira
     vel_DE = 0,   //Velocidade da roda dianteira esquerda
     vel_DD = 0,   //Velocidade da roda dianteira direita
     vel_TE = 0,   //Velocidade da roda traseira esquerda
     vel_TD = 0,   //Velocidade da roda traseira direita
     RPM = 0,
     Beacon = 0;

/*Variáveis do Pacote 2 -> 30Hz*/
unsigned long ext1_DE = 0, //Extensômetro 1 da placa dianteira esquerda
       ext2_DE = 0, //Extensômetro 2 da placa dianteira esquerda
       ext3_DE = 0, //Extensômetro 3 da placa dianteira esquerda
       ext1_DD = 0, //Extensômetro 1 da placa dianteira direita
       ext2_DD = 0, //Extensômetro 2 da placa dianteira direita
       ext3_DD = 0, //Extensômetro 3 da placa dianteira direita
       ext1_TE = 0, //Extensômetro 1 da placa traseira esquerda
       ext2_TE = 0, //Extensômetro 2 da placa traseira esquerda
       ext3_TE = 0, //Extensômetro 3 da placa traseira esquerda
       ext1_TD = 0, //Extensômetro 1 da placa traseira dianteira
       ext2_TD = 0, //Extensômetro 2 da placa traseira dianteira
       ext3_TD = 0; //Extensômetro 3 da placa traseira dianteira

/*Variáveis do Pacote 3 -> 30Hz*/
uint16_t TPS = 0,       //TPS
     OILP = 0,      //Pressão de Óleo
     FUELP = 0,     //Pressão de Combustível
     VAZBICOS = 0,    //Vazão dos Bicos
     PoSus_DE = 0,    //Posição da suspensão da placa dianteira esquerda
     PoSus_DD = 0,    //Posição da suspensão da placa dianteira direita
     PoSus_TE = 0,    //Posição da suspensão da placa traseira esquerda
     PoSus_TD = 0,    //Posição da suspensão da placa traseira dianteira
     PosVolante = 0,  //Posição do volante
     BatCor = 0,    //Corrente da Bateria
     VentCor = 0,     //Corrente da Ventoinha
     BombCor = 0,     //Corrente da Bomba
     PresFreio_D = 0,   //Pressão do Freio Dianteiro
     PresFreio_T = 0;   //Pressão do Freio Traseiro

/*Variáveis do Pacote 4 -> 10Hz*/
uint16_t BAT = 0,
     ECT = 0,
     OILT = 0,
     Tempdisco_DE = 0,
     Tempdisco_DD = 0,
     Tempdisco_TE = 0,
     Tempdisco_TD = 0,
     TempVentoinha = 0,
     TempBomba = 0,
     PosRunners = 0,
     AcioVent = 0,
     AcioBomba = 0,
     AcioMata = 0;
uint32_t GPS_Lat = 0, //GPS.lat*100;
     GPS_Long = 0; //GPS.long*100;
char   GPS_NS = 'N',
     GPS_EW = 'E',
        hgpshour = 0,
    hgpsminute = 0,
    hgpsseconds = 0,
    hgpsmilliseconds = 0,
     hgpsyear = 0,
   hgpsmonth = 0,
   hgpsday;


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

 acelX_DE = i*250;
 acelY_DE = j*250;
 acelZ_DE = i*250;
 acelX_DD = -i*250;
 acelY_DD = -j*250;
 acelZ_DD = -i*250;

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
Serial.write(buffer1, 37);
if (TIMERCOUNT%2 == 0){
  Serial.write(buffer2, 34);
  Serial.write(buffer4, 42);
}
if(TIMERCOUNT%20 == 0){
  Serial.write(buffer3, 42);
 }
TIMERCOUNT++;
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
    buffer1[27]= vel_DE;
    buffer1[28]= vel_TD;
    buffer1[29]= vel_TE;
    buffer1[30]= RPM>>8;
    buffer1[31]= RPM;
    buffer1[32]= Beacon;
    buffer1[33] = TIMERCOUNT>>8;
    buffer1[34] = TIMERCOUNT;
    buffer1[35] = 9;
    buffer1[36] = '\n';

    buffer2[0] = 2;
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

    buffer3[0] = 3;
    buffer3[1] = 5;
    buffer3[2] = BAT>>8; //max1500
    buffer3[3] = BAT;
    buffer3[4] = ECT>>8;
    buffer3[5] = ECT;
    buffer3[6] = OILT>>8;
    buffer3[7] = OILT;
    buffer3[8] = Tempdisco_DE>>8;
    buffer3[9] = Tempdisco_DE;
    buffer3[10] = Tempdisco_DD>>8;
    buffer3[11] = Tempdisco_DD;
    buffer3[12] = Tempdisco_TE>>8;
    buffer3[13] = Tempdisco_TE;
    buffer3[14] = Tempdisco_TD>>8;
    buffer3[15] = Tempdisco_TD;
    buffer3[16] = TempVentoinha>>8;
    buffer3[17] = TempVentoinha;
    buffer3[18] = TempBomba>>8;
    buffer3[19] = TempBomba;
    buffer3[20] = PosRunners>>8;
    buffer3[21] = PosRunners;
    buffer3[22] = (AcioVent>>8) | (AcioBomba<<7) | (AcioMata<<5);
    buffer3[23] = GPS_Lat>>16;
    buffer3[24] = GPS_Lat>>8;
    buffer3[25] = GPS_Lat;
    buffer3[26] = GPS_Long>>16;
    buffer3[27] = GPS_Long>>8;
    buffer3[28] = GPS_Long;
    buffer3[29] = GPS_NS;
    buffer3[30] = GPS_EW;
    buffer3[31] = hgpshour;
    buffer3[32] = hgpsminute;
    buffer3[33] = hgpsseconds;
    buffer3[34] = hgpsmilliseconds;
    buffer3[35] = hgpsyear;
    buffer3[36] = hgpsmonth;
    buffer3[37] = hgpsday;
    buffer3[38] = TIMERCOUNT>>8;
    buffer3[39] = TIMERCOUNT;
    buffer3[40] = 9;
    buffer3[41] = '\n';

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
    buffer4[38] = TIMERCOUNT>>8;
    buffer4[39] = TIMERCOUNT; 
    buffer4[40] = 9;
    buffer4[41] = 10;  
}
