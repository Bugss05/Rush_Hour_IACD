'''
Este script contém as classes Carros e Node, que são usadas para representar os carros e os nós no algoritmo de busca, respectivamente.'''


import copy
from matriz_dos_problemas import *

class Carros:   
    def __init__(self,cor:int, linha: int, coluna: int, orientacao: str, tabuleiro: list, tamanho: int) -> None:
        self.cor = cor  # Cor do carro
        self.linha = linha  # Linha em que o carro está
        self.coluna = coluna  # Coluna em que o carro está
        self.orientacao = orientacao  # Orientação do carro (horizontal ou vertical)
        self.tabuleiro = tabuleiro  # Tabuleiro do jogo
        self.tamanho = tamanho  # Tamanho do carro

    def possiveis_coordenadas(self):  # Retorna uma lista de coordenadas possíveis para o próximo movimento do carro
        if self.orientacao == "horizontal":
            coordenadas = Carros.coordenada_horizontal(self, self.linha, self.coluna, self.tabuleiro, self.tamanho)
        else:
            coordenadas = Carros.coordenada_vertical(self, self.linha, self.coluna, self.tabuleiro, self.tamanho)
        # Achatamos a lista de movimentos e removemos quaisquer listas vazias
        # Isso é feito iterando sobre cada sublista na lista de movimentos
        # Se a sublista não estiver vazia, cada coordenada na sublista é adicionada à nova lista
        flattened_moves = []
        for sublist in coordenadas:
            if sublist:  # Verifica se a sublista não está vazia
                for coord in sublist:
                    flattened_moves.append(coord)
        return flattened_moves
    
    def possiveis_movimentos(self):  # Retorna uma lista de movimentos possíveis para o próximo movimento do carro
        if self.orientacao == "horizontal":
            movimentos = Carros.movimento_horizontal(self, self.linha, self.coluna, self.tabuleiro, self.tamanho)
        else:
            movimentos = Carros.movimento_vertical(self, self.linha, self.coluna, self.tabuleiro, self.tamanho)
        # Achatamos a lista de movimentos e removemos quaisquer listas vazias
        # Isso é feito iterando sobre cada sublista na lista de movimentos
        # Se a sublista não estiver vazia, cada coordenada na sublista é adicionada à nova lista
        flattened_moves = []
        for sublist in movimentos:
            if sublist:  # Verifica se a sublista não está vazia
                for coord in sublist:
                    flattened_moves.append(coord)
        return flattened_moves
    
    def coordenada_horizontal(self, linha, coluna, tabuleiro, tamanho):  # Retorna uma lista de coordenadas possíveis para movimento horizontal
        lista_de_movimentos = [
            Carros.mover_para_esquerda(self, linha, coluna, tabuleiro, tamanho)[1],
            Carros.mover_para_direita(self, linha, coluna, tabuleiro, tamanho)[1]]
        return lista_de_movimentos
    
    def coordenada_vertical(self, linha, coluna, tabuleiro, tamanho):  # Retorna uma lista de coordenadas possíveis para movimento vertical
        lista_de_movimentos = [
            Carros.mover_para_cima(self, linha, coluna, tabuleiro, tamanho)[1],
            Carros.mover_para_baixo(self, linha, coluna, tabuleiro, tamanho)[1]]
        return lista_de_movimentos
    
    def movimento_horizontal(self, linha, coluna, tabuleiro, tamanho):  # Retorna uma lista de movimentos possíveis para movimento horizontal
        lista_de_movimentos = [
            Carros.mover_para_esquerda(self, linha, coluna, tabuleiro, tamanho)[0],
            Carros.mover_para_direita(self, linha, coluna, tabuleiro, tamanho)[0]]
        return lista_de_movimentos
    
    def movimento_vertical(self, linha, coluna, tabuleiro, tamanho):  # Retorna uma lista de movimentos possíveis para movimento vertical
        lista_de_movimentos = [
            Carros.mover_para_cima(self, linha, coluna, tabuleiro, tamanho)[0],
            Carros.mover_para_baixo(self, linha, coluna, tabuleiro, tamanho)[0]]
        return lista_de_movimentos
    
    def mover_para_esquerda(self, linha, coluna, tabuleiro, tamanho):  # Implementa a lógica de mover para a esquerda
        tabuleiro2 = []
        tabuleiro2 = copy.deepcopy(tabuleiro)
        lista_tabuleiros = []  # Lista de tabuleiros
        lista_de_lances = []  # Lista de lances
        for i in range(coluna):
            if 0 <= linha <= 5 and 1 <= coluna <= 5 and tabuleiro2[linha][coluna-1] == ".":  # Troca de posições
                tabuleiro2[linha][coluna + (tamanho - 1)], tabuleiro2[linha][coluna - 1] = tabuleiro2[linha][coluna-1], tabuleiro2[linha][coluna +(tamanho - 1)]
                tabuleiro1 = copy.deepcopy(tabuleiro2)
                coluna -= 1  # Atualiza a coluna que estamos a analisar
                lista_de_lances.append((coluna, linha))
                lista_tabuleiros.append(tabuleiro1)  # Adiciona a nova posição
            else:
                break  # Significa que há um carro à frente ou chegou à borda
        return [lista_tabuleiros, lista_de_lances]
    
    def mover_para_direita(self, linha, coluna, tabuleiro, tamanho):  # Implementa a lógica de mover para a direita
        tabuleiro2 = []
        tabuleiro2 = copy.deepcopy(tabuleiro)
        lista_tabuleiros = []  # Lista de tabuleiros
        lista_de_coordenadas = []  # Lista de coordenadas
        for i in range((5-coluna)-(tamanho-1)):
            if 0 <= linha <= 5 and 0 <= coluna <= 5-tamanho and tabuleiro2[linha][coluna+tamanho] == ".":  # Troca de posições    
                tabuleiro2[linha][coluna], tabuleiro2[linha][coluna + tamanho] = tabuleiro2[linha][coluna + tamanho], tabuleiro2[linha][coluna]
                tabuleiro1 = copy.deepcopy(tabuleiro2)
                lista_tabuleiros.append(tabuleiro1)  # Adiciona a nova posição
                coluna += 1  # Atualiza a coluna que estamos  a analisar
                
                lista_de_coordenadas.append((coluna, linha))
            else:
                break  # Significa que há um carro à frente ou chegou à borda
        return [lista_tabuleiros, lista_de_coordenadas]
    
    def mover_para_cima(self, linha, coluna, tabuleiro, tamanho):  # Implementa a lógica de mover para cima
        tabuleiro2 = []
        tabuleiro2 = copy.deepcopy(tabuleiro)
        lista_tabuleiros = []  # Lista de tabuleiros
        lista_de_coordenadas = []  # Lista de coordenadas
        for i in range(linha):
            if 1 <= linha <= 5 and 0 <= coluna <= 5 and tabuleiro2[linha-1][coluna] == ".":  # Troca de posições
                tabuleiro2[linha - 1][coluna], tabuleiro2[linha + (tamanho - 1)][coluna] = tabuleiro2[linha + (tamanho - 1)][coluna], tabuleiro2[linha - 1][coluna]
                linha -= 1  # Atualiza a linha que estamos  a analisar
                tabuleiro1 = copy.deepcopy(tabuleiro2)
                lista_tabuleiros.append(tabuleiro1)  # Adiciona a nova posição
                lista_de_coordenadas.append((coluna, linha))
            else:
                break  # Significa que há um carro à frente ou chegou à borda
        return [lista_tabuleiros, lista_de_coordenadas]   
    
    def mover_para_baixo(self, linha, coluna, tabuleiro, tamanho):  # Implementa a lógica de mover para baixo
        tabuleiro2 = []
        tabuleiro2 = copy.deepcopy(tabuleiro)
        lista_tabuleiros = []  # Lista de tabuleiros
        lista_de_coordenadas = []  # Lista de coordenadas
        for i in range((5-linha)-(tamanho-1)):
            if 0 <= linha <= 5-tamanho and 0 <= coluna <= 5 and tabuleiro2[linha+tamanho][coluna] == ".":  # Troca de posições
                tabuleiro2[linha + tamanho][coluna], tabuleiro2[linha][coluna] = tabuleiro2[linha][coluna], tabuleiro2[linha + tamanho][coluna]
                tabuleiro1 = copy.deepcopy(tabuleiro2)
                linha += 1  # Atualiza a linha que estamos  a analisar
                lista_tabuleiros.append(tabuleiro1)  # Adiciona a nova posição
                lista_de_coordenadas.append((coluna, linha))        
            else:
                break  # Significa que há um carro à frente ou chegou à borda


        return [lista_tabuleiros, lista_de_coordenadas]
    
    
    @classmethod
    
    def coordenada1e2(cls, cor:int, tamanho:int, x:int, y:int, orientaçao:int, tabuleiro: list):  # Construtor da classe 
        if orientaçao == 1:
            orientacao = "vertical"
        else:
            orientacao = "horizontal"
        return cls(cor, y, x, orientacao, tabuleiro, tamanho)  # Retorna a classe já transformada


class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        """
        Classe que representa um nó no algoritmo de busca.

        Args:
            state (list): O estado atual do nó.
            parent (Node, optional): O nó pai. Defaults to None.
            g (int, optional): O custo acumulado do caminho do nó inicial até o nó atual. Defaults to 0.
            h (int, optional): O valor da heurística do nó. Defaults to 0.
        """
        self.state = state  # Armazena o estado atual do nó
        self.parent = parent  # Armazena o nó pai
        self.g = g  # Armazena o custo acumulado do caminho do nó inicial até o nó atual
        self.h = h  # Armazena o valor da heurística do nó
        self.f = self.g + self.h  # Calcula o valor da função de avaliação f(n) = g(n) + h(n)
        self.depth = g//0.5  # Calcula a profundidade do nó dividindo o custo acumulado por 0.5

    def __eq__(self, other):
        """
        Verifica se dois nós são iguais.

        Args:
            other (Node): O outro nó a ser comparado.

        Returns:
            bool: True se os nós são iguais, False caso contrário.
        """
        if isinstance(other, Node):
            return self.state == other.state
        return False

    def __hash__(self):
        """
        Retorna o hash do nó.

        Returns:
            int: O hash do nó.
        """
        return hash(tuple(map(tuple, self.state)))

    def get_children(self):
        """
        Gera os filhos do nó.

        Yields:
            Node: Um nó filho.
        """
        for child in todas_posições_possiveis_a(self.state):
            yield Node(child, parent=self, g=0, h=0)

    def is_goal(self):
        """
        Verifica se o nó é o objetivo.

        Returns:
            bool: True se o nó é o objetivo, False caso contrário.
        """
        if lista_de_carros(self.state)[2].coluna == 4:
            return True
        return False

    def get_path(self):
        """
        Retorna o caminho do nó até o nó inicial.

        Returns:
            list: Uma lista de nós representando o caminho.
        """
        path = []
        node = self
        while node is not None:
            path.append(node)
            node = node.parent
        return path[::-1]

def todas_posições_possiveis_a(tabuleiro:list)->list:
    lista_inteira=[]  # Cria uma lista vazia para armazenar todas as posições possíveis
    dic_carros=lista_de_carros(tabuleiro)  # Obtém um dicionário de carros a partir do tabuleiro
    for i in dic_carros.values():  # Itera sobre os valores do dicionário de carros
        lista_inteira.append(i.possiveis_movimentos())  # Adiciona os movimentos possíveis de cada carro à lista
    flattened_moves = []  # Cria uma lista vazia para armazenar os movimentos achatados
    for sublist in lista_inteira:  # Itera sobre cada sublista na lista de movimentos
        if sublist:  # Verifica se a sublista não está vazia
            for coord in sublist:  # Itera sobre cada coordenada na sublista
                flattened_moves.append(coord)  # Adiciona a coordenada à lista de movimentos achatados
    return flattened_moves  # Retorna a lista de movimentos achatados

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

def lista_de_carros(tabuleiro: list) -> dict:# transformar a matriz em classes Carros por dicionairo de cores 
    carros = []
    qntd_d_cd_carro = {}  # criar um dicionario que para cada carro esta associado o seu tamanho
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):  # analisar matriz
            if tabuleiro[i][j] != ".":
                if tabuleiro[i][j] not in qntd_d_cd_carro:  # adicionar cor se nao existir
                    qntd_d_cd_carro[tabuleiro[i][j]] = [0,j,i,0] # [tamanho, coluna, linha, orientação]
                elif qntd_d_cd_carro[tabuleiro[i][j]][0] == 1: # se for a segunda coordenada
                    if tabuleiro [i-1][j]== tabuleiro[i][j]: # se for vertical
                        qntd_d_cd_carro[tabuleiro[i][j]][3]=1  # se for vertical
                qntd_d_cd_carro[tabuleiro[i][j]][0]+=1 # aumentar o tamanho do carro    
    for cor, carro in qntd_d_cd_carro.items():#buscar o tuple de cada carro
        carro = Carros.coordenada1e2(cor,carro[0],carro[1],carro[2],carro[3], tabuleiro)#tranformar em classe Carros
        carros.append(carro)# Lista das classses Carros
    return lista_para_dicionario(carros) #para chamar carros: carros[indice aonde esta o carro].possiveis_movimentos()

