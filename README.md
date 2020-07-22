# Telemetria

![print1](/Images/interface_screenshot.png)

## Como utilizar
### Arquivos

Baixe os arquivos do repositório. O executável do programa se encontra na pasta *dist*, com o nome interface19.exe. Recomendo criar um atalho para esse .exe caso não queira abrir essa pasta sempre que for utilizar o programa. Para executar e utilizar o programa, só é necessário baixar a pasta *dist*.

### Utilizando o programa
## Configurações

![print2](/Images/serial_port_stream.png)

Selecione a porta serial na qual está conectado o dispositivo receptor (como o Xbee, arduino, etc.). Se ela não aparecer na lista imediatamente, o botão *update ports* pode ser utilizado para recarregar a lista.

Em seguida, confira se o Baud Rate da comunicação está configurado com o mesmo valor do Baud Rate do dispositivo receptor.

O *update time* é o tempo, em segundos, entre o fim de uma atualização da interface e o inicio da próxima. Nesse caso, a atualização da interface não se refere à atualização dos campos de dados, mas  à frequência de chamada da função principal, que é responsável por executar todos os comandos, como leitura da porta serial, gravação no arquivo, etc.

O *update counter* é uma configuração auxiliar que permite que o usuário escolha a frequência de atualização dos dados de cada pacote, para melhorar o desempenho do programa. Se em P1 estiver configurado em 6, isso quer dizer que a interface vai esperar receber 6 frames do pacote 1 para atualizar os dados do respectivo pacote. Isso não interfere no processo de gravação: todos os 6 valores não mostrados dos dados estarão registrados no arquivo de gravação da mesma forma.

Em *Data Stream*, é possível verificar os pacotes de dados recebidos. A configuração *apply functions* permite alternar a visualização dos dados entre sua forma "crua", ou seja, da mesma forma como foi enviado pelo carro, ou convertidos para suas respectivas unidades de engenharia.

![print3](/Images/alarm_wheel.png)

É possível também configurar alarmes para cada um dos dados. Basta selecionar o dado, o valor, o tipo de alarme (maior que, menor que ou igual ao valor) e salvar. Assim, seu respectivo campo na interface ficará vermelho caso o alarme seja acionado.

Os valores máximo e mínimo da posição de volante correspondem ao valor lido quando o volante está todo para a direita ou para a esquerda.


![print4](/Images/file_settings.png)

É necessário sempre colocar as taxas de envio (as taxas de amostragem) de cada pacote para que o arquivo de gravação possa ser utilizado posteriormente. Os outros campos são opcionais, mas é recomendado que o usuário sempre preencha o máximo que conseguir. É possível salvar os valores em *save values* para que eles não tenham que ser redigitados em uma próxima execução da interface. *File Name* é o nome do arquivo .txt no qual serão gravados os dados recebidos.

## Desenvolvimento
### Dependencias

Baixar python e adicionar às variáveis de ambiente (PATH). Instalar os módulos:

```
Módulo python - comando pip para instalação

matplotlib - pip install matplotlib
numpy - pip install numpy
pyqt5-tools - pip install pyqt5-tools
PyQt5
pyqtgraph - pip install pyqtgraph
```

O pyqt5-tools instala também o Qt Designer, ferramenta utilizada para criar o visual da interface

### Modificando a interface

Para modificar algo na interface, altere o arquivo interface.ui, salve, e execute o seguinte comando:

```
pyuic5 -x interface.ui -o interface_generated.py
```

Após executar o comando, procure a linha <from pyqtgraph import PlotWidget>, no arquivo interface_generated.py,
(deve estar antes da declaracao <if __name__ == "__main__":>, no fim do arquivo), recorte ela e cole após a
declaracao <from PyQt5 import QtCore, QtGui, QtWidgets>, no inicio do arquivo. Isso deve ser feito após qualquer
alteracao no Qt Designer para que ela tenha efeito no codigo, de forma a evitar o erro no qual nao é reconhecido o modulo pyqtgraph.

### Gerando o executável

Rodar comando (necessário o módulo pyinstaller)

```
pyinstaller interface19.py
```

O executável estará salvo na pasta dist.

### Classes

Ui_MainWindow - criada automaticamente executando a linha de comando vista acima, é responsavel por mostrar a interface. Os campos e mostradores sao acessados por meio de sua instancia única, <ui>, assim como os connects dos sinais (como aperto de botoes)

Log - Classe criada para facilitar escritas em campos com muito texto. Escreve mensagens na instancia logInstance, dada como parametro construtor. O texto escrito é mostrado primeiro, e os textos escritos anteriormente sao mostrados em seguida, todos separados por quebra de linha. A instancia logInstance é um campo da interface que aceite o método setText.

File - Facilita operacoes em arquivo. Já cria um arquivo com a hora e o minuto concatenado.

Data - Armazena os dados em um dicionario <dic>. O dicionario <dicRaw> armazena os mesmos dados, porém em sua versao "crua", sem nenhum processamento. O processamento do vetor <buffer> recebido é feito das funcoes updatePxData. Há também um dicionario que armazena os alarmes, na forma {chave: [valor, tipo]} (exemplo: {'ect':[95, greater than]}). Classe tambem armazena vetores dos dados que necessitam, como dados que vao ser plotados em graficos.

Program - Classe responsavel por executar o programa que le continuamente da porta serial e chama funcoes de atualizar os dados na classe Data e na interface.

Interface - Embora nao seja uma classe, todas as funcoes que mexem diretamente com campos da interface estao implementadas arquivo principal (main), que é executado. Isso inclui funcoes que atualizam campos e mostradores e funcoes que sao chamadas quando algum botao é pressionado.

settings - Instancia de QtCore.QSettings, com ela é possivel salvar no PC do usuário informacoes de campos editados na interface, e resgatá-los na proxima esecucao do programa.


![UML](/Images/UML.png)
