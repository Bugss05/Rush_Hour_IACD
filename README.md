# <font size="80">Rush Hour</font>
*******
Trabalho realizado por:

* Afonso Coelho (FCUP_IACD:202305085)
* Diogo Amaral (FCUP_IACD:202305187) 
* Miguel Carvalho (FCUP_IACD:202305229)
<div style="padding: 10px;padding-left:5%">
<img src="fotos_md/Cienciasporto.png" style="float:left; height:75px;width:200px">
<img src="fotos_md/Feuporto.png" style="float:left ; height:75px; padding-left:20px;width:200px">
</div>

<div style="clear:both;"></div>

******
### SOBRE O PROJETO 
No primeiro ano da Licenciatura em Inteligência Artificial e Ciência de Dados, na Faculdade de Ciências da Universidade do Porto, ficamos encarregues de desenvolver uma AI que fosse capaz de resolver um jogo de tabuleiro single player, neste caso, o Rush Hour. O objetivo deste projeto é o desenvolvimento algorítimico de diferentes métodos de pesquisa, avaliando entre si algumas métricas como o tempo de execução `(Time Complexity)` e a quantidade de nós expandidos `(Space Complexity)`, em busca do método mais ótimo para a resolução de qualquer posição resolvível do tabuleiro. Eis os métodos de pesquisa:<br>

* Depth-First Search (DFS)
* Breadth-First Search (BFS)
* A Star (A*)
* Iterative Deepening Search (IDS)


Nesta página, existe um diretório [/Game](/Game) que salvaguarda uma interface simples dos problemas bem como a implementação gráfica dos Algoritmos de Pesquisa progamados. A página inicial contém os programas de construção das estatísticas. <br>As estatísticas completas estão no ficheiro excel [Stats.xlsx](Stats.xlsx)

>Para aceder à documentação completa e formalização do problema, deve por favor abrir o ficheiro [Rush_Hour_Documentacao.docx](Rush_Hour_Documentacao.docx)


## Como fazer o download e utilizar a interface  
#### Primeiro passo:
Extraia o .zip da página github e descomprima o ficheiro
#### Segundo passo: 
Instale `numpy` no diretório pelo terminal 
```
pip install numpy
```
#### Terceiro passo: **IMPORTANTE** 
Entre no diretório do ficheiro rush_hour.py pelo terminal (no folder [/Game](/Game)) 
```
cd (diretório da pasta)
```
#### Quarto passo 
Corra o programa 
```
python3 rush_hour.py
```
*****

## Sobre a utilização de ficheiros

#### Criar problemas 
Caso queira criar novos problemas para que a AI os resolva, basta abrir o seguinte programa [builder_de_problemas.py](builder_de_problemas.py). Para o bom funcionamento do programa, evite repetir os números dos problemas já existentes `(1-80)` e, para verificar a correta imputação do problema, considere comparar a sua matriz criada no ficheiro [problemas.txt](problemas.txt).<br>Ao executar o ficheiro [builder_de_problemas.py](builder_de_problemas.py), deve seguir as seguintes diretrizes como atenta o seguinte exemplo:


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
cor de [3,13], 2 se for o carro vermelho (tamanho 2) [14,18] (tamanho 3)

>Se não estiver familiarizado com o conceito de `cabeça do carro` por favor consultar o ficheiro da documentação do problema.
 
******

#### Utilizar os métodos de pesquisa 
Deve escolher um dos 4 ficheiros de pesquisa e, posteriormente, eleger o número do problema a resolver. A sua respetiva resolução estará presente no ficheiro [output.txt](output.txt) e as suas estatísticas no [estatisticas.txt](estatisticas.txt).
