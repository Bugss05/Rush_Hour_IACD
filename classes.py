'''
cada carro tem uma cor e é inicializado como tal
carro_vermelho= [2,tamanho,tabuleiro]---> cor do carro,tamanho, tabuleiro 
a classmethod transforma a cor do carro e localiza a cabeça do carro e a orientação dele localizando a segunda coordenada do carro visto que todos os carros têm pelo menos duas coordenadas


'''


class Carros:   
    def __init__(self,cor:int, linha: int, coluna: int, orientacao: str, tabuleiro: list, tamanho: int) -> None:
        self.cor = cor
        self.linha = linha
        self.coluna = coluna
        self.orientacao = orientacao
        self.tabuleiro = tabuleiro
        self.tamanho = tamanho
 
    def possiveis_movimentos(self):
        if self.orientacao == "horizontal":
            return Carros.movimento_horizontal(self, self.linha, self.coluna, self.tabuleiro, self.tamanho)
        else:
            return Carros.movimento_vertical(self, self.linha, self.coluna, self.tabuleiro, self.tamanho)
    def movimento_horizontal(self, linha, coluna, tabuleiro, tamanho):
        lista_de_movimentos = [Carros.mover_para_esquerda(self, linha, coluna, tabuleiro, tamanho), Carros.mover_para_direita(self, linha, coluna, tabuleiro, tamanho)]
        return lista_de_movimentos
    def movimento_vertical(self, linha, coluna, tabuleiro, tamanho):
        lista_de_movimentos = [Carros.mover_para_cima(self, linha, coluna, tabuleiro, tamanho), Carros.mover_para_baixo(self, linha, coluna, tabuleiro, tamanho)]
        return lista_de_movimentos
    def mover_para_esquerda(self, linha:int, coluna:int, tabuleiro:int, tamanho:int):# Implementar a lógica de mover para a esquerda
        lista_tabuleiros:list = []#lista de lances
        for i in range(coluna):
            if 0<=linha<=5 and 1<=coluna<=5 and tabuleiro[linha][coluna-1] == 0:#trocar de posições 
                tabuleiro[linha][coluna + (tamanho - 1)], tabuleiro[linha][coluna - 1] = tabuleiro [linha][coluna], tabuleiro[linha + (tamanho - 1)][coluna - 1]
                coluna += 1#atualizar a coluna que estamos a analisar
                lista_tabuleiros.append(tabuleiro)
            else:
                break#quer dizer que tem um carro à frente ou chegou à borda 
        if len(lista_tabuleiros)==0:
            return None
        return lista_tabuleiros
    def mover_para_direita(self, linha, coluna, tabuleiro, tamanho):# Implementar a lógica de mover para a direita
        lista_tabuleiros:list = []#lista de lances
        for i in range ((5-coluna)-(tamanho-1)):
            if 0<=linha<=5 and 0<=coluna<=5-tamanho and tabuleiro[linha][coluna+tamanho] == 0:#trocar de posições
                tabuleiro[linha][coluna], tabuleiro[linha][coluna + tamanho] =tabuleiro [linha][coluna + tamanho], tabuleiro[linha][coluna]
                coluna -= 1#atualizar a coluna que estamos a analisar
                lista_tabuleiros.append(tabuleiro)#adicionar a nova posiçao
            else:
                break#quer dizer que tem um carro à frente ou chegou à borda 
        if len(lista_tabuleiros)==0:
            return None
        return lista_tabuleiros
    def mover_para_cima(self, linha, coluna, tabuleiro, tamanho):# Implementar a lógica de mover para cima
        lista_tabuleiros:list = []#lista de lances
        for i in range (linha):
            if 1<=linha<=5 and 0<=coluna<=5 and tabuleiro[linha-1 ][coluna] == 0:#trocar de posições
                tabuleiro[linha - 1][coluna], tabuleiro[linha + (tamanho - 1)][coluna] =tabuleiro[linha + (tamanho - 1) ][coluna] , tabuleiro[linha - 1] [coluna]
                linha+=1#atualizar a linha que estamos a analisar
                lista_tabuleiros.append(tabuleiro)#adicionar a nova posiçao
            else:
                break#quer dizer que tem um carro à frente ou chegou à borda
        if len(lista_tabuleiros)==0:
            return None
        return lista_tabuleiros   
    def mover_para_baixo(self, linha, coluna, tabuleiro, tamanho):# Implementar a lógica de mover para baixo
        lista_tabuleiros:list = []#lista de lances
        for i in range ((5-linha)-(tamanho-1)):
            if 0<=linha<=5-tamanho and 0<=coluna<=5 and tabuleiro[linha+tamanho][coluna] == 0:#trocar de posições
                tabuleiro[linha + tamanho][coluna], tabuleiro[linha][coluna] = tabuleiro [linha][coluna], tabuleiro[linha + tamanho][coluna]
                linha-=1#atualizar a linha que estamos a analisar
                lista_tabuleiros.append(tabuleiro)#adicionar a nova posiçao
            else:
                break#quer dizer que tem um carro à frente ou chegou à borda
        if len(lista_tabuleiros)==0:
            return None
        return lista_tabuleiros
    @classmethod
    def coordenada1e2(cls,cor:int,tamanho:int,tabuleiro: list):
        contador=0
        orientacao=None
        x = None
        y = None
        for linha in range(len(tabuleiro[0])):#explorar todas as linhas do tabuleiro
            for coluna in range(len(tabuleiro[0])):#explorar todas as colunas do tabuleiro
                if tabuleiro[linha][coluna] == cor:#encontrou o carro que estamos à procura
                    if contador==0:# primeiro para saber a cabeça do carro
                        x=coluna
                        y=linha
                        contador+=1
                    elif contador==1:# segundo para saber a orientação do carro
                        if x == coluna:
                            orientacao = "vertical"
                        elif y == linha:
                            orientacao = "horizontal"
                        contador=0
        return cls(cor,y,x,orientacao,tabuleiro,tamanho)#retornar a classe ja transformada
    
def lista_de_carros(tabuleiro: list) -> list:
    carros = []
    qntd_d_cd_carro = {}  # criar um dicionario que para cada carro esta associado o seu tamanho
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):  # analisar matriz
            if tabuleiro[i][j] != 0:
                if tabuleiro[i][j] not in qntd_d_cd_carro:  # adicionar cor se nao existir
                    qntd_d_cd_carro[tabuleiro[i][j]] = 0
                qntd_d_cd_carro[tabuleiro[i][j]] += 1  # adicionar tamanho
    for cor, tamanho in qntd_d_cd_carro.items():#buscar o tuple de cada carro
        carro = Carros.coordenada1e2(cor, tamanho, tabuleiro)#tranfosmar em classe Carros
        carros.append(carro)# Lista das classses Carros
    return carros #para chamar carros: carros[indice aonde esta o carro].possiveis_movimentos()
matrix =[
    [8, 8, 0, 7, 0, 0],
    [3, 3, 0, 7, 16, 17],
    [0, 2, 2, 15, 16, 17],
    [4, 4, 6, 15, 16, 17],
    [5, 0, 6, 15, 0, 0],
    [5, 0, 0, 14, 14, 14],
]

def lista_para_dicionario(lista_ordenada: list) -> dict:
    """
    Converte uma lista ordenada de objetos Carros em um dicionário, onde as chaves são as cores dos carros e os valores são listas de objetos Carros com a mesma cor.

    Args:
        lista_ordenada (list): Lista ordenada de objetos Carros.

    Returns:
        dict: Dicionário onde as chaves são as cores dos carros e os valores são listas de objetos Carros com a mesma cor.
    """
    dicionario_de_carros = {}
    for carro in lista_ordenada:
        cor = carro.cor
        dicionario_de_carros[cor]=carro
    return dicionario_de_carros
# Exemplo de uso:
TODOS_OS_CARROS = lista_para_dicionario((lista_de_carros(matrix)))
print(TODOS_OS_CARROS[2].linha,TODOS_OS_CARROS[2].coluna)
