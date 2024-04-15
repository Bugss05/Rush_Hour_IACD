# <font size="80">Rush Hour</font>
*******
Trabalho realizado por:

* Afonso Coelho (FCUP_IACD:202305085)
* Diogo Amaral (FCUP_IACD:202305187) 
* Miguel Carvalho (FCUP_IACD:202305229)

******
### PROJETO 
O projeto foi proposto na cadeira de Elementos de Inteligência Artificial e Ciência de Dados (ano 1) e tem como objetivo apresentar, analisar e implementar uma inteligência artificial (IA) capaz de resolver o jogo "Rush Hour", de acordo com vários algoritmos já conhecidos, avaliando métricas como o tempo de execução e a quantidade de nós expandidos, no sentido de definir qual o algoritmo mais ótimo para este jogo.:<br>

*  Depth-First Search (DFS)
* Breadth-First Search (BFS)
* A*
* Iterative Deepening Search (IDS)

Existe um diretório [/Game](/Game) que consiste num interface simples dos problemas bem como a implementação gráfica dos Algoritmos de Pesquisa progamados. A página inicial contem os programas de construção das estatísticas. <br>As estatísticas completas estão no ficheiro excel [Stats.xlsx](Stats.xlsx)

>Para aceder à decomentação competa e formalização do problema por favor abrir o ficheiro [Rush_Hour_Documentação.docx](Rush_Hour_Documentação.docx)


## Como fazer o download e utilizar o interface  
#### Primeiro passo 
Extrair o .zip da página github e descomprimir o ficheiro
#### Segundo passo 
Instalar `numpy` no diretório pelo terminal 
```
pip install numpy
```
#### Terceiro passo **IMPORTANTE** 
Entrar no diretório do ficheiro rush_hour.py pelo terminal (no folder [/Game](/Game)) 
```
cd (diretório da pasta)
```
#### Quarto passo 
Correr o programa 
```
python3 rush_hour.py
```
*****

## Como utilizar ficheiros

#### Criar problemas 
No ficheiro [builder_de_problemas.py](builder_de_problemas.py) pode criar qualquer problema. Evite repetir números de problemas ja existentes e considere comparar a matriz criada no ficheiro [problemas.txt](problemas.txt) para confirmar a correspondencia do input dado.<br>Cada carro tem as seguintes perguntas 


``` 
qual é a posição x? 
```
 posição x da cabeça do carro na matriz [0,5]
```
qual é a posição y?
``` 
posição x da cabeça do carro na matriz [0,5]
```
qual é a orientação (0=H)?
```
0= Horizontal, 1= Vertical
```
qual é a cor?
```
cor de [3,13] (tamanho 2) [14,18] (tamanho 4)

<br>
>se nao estiver familiarizado com o conceito de cabeça do carro por favor consultar o ficheiro da decomentação do problema
 
******

#### Utilizar os métodos de pesquisa 
Escolher um dos 4 ficheiros de pesquisa e  depois escolher um número do problema. A sua respetiva resolução estará presente no ficheiro [output.txt](output.txt) e as suas estatísticas no [estatisticas.txt](estatisticas.txt) 
