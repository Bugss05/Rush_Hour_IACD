'''Pesquisa A*'''

from collections import deque
from classes import *
import time
import math
import itertools


problem = int(input("qual é o problema? "))
matrix1= problema(problem)

BOARD_COLUMNS = 6

def a_star(start):
    start_time = time.time()  # Regista o tempo de início da busca
    open_list = [start]  # Lista de nós abertos
    closed_list = []  # Lista de nós fechados
    nodes_searched = 0  # Contador de nós explorados

    while open_list:
        open_list.sort(key=lambda node: node.f)  # Ordena a lista de nós abertos pelo valor de f
        current_node = open_list.pop(0)  # Remove o nó com menor valor de f da lista de nós abertos
        closed_list.append(current_node)  # Adiciona o nó atual à lista de nós fechados

        if current_node.is_goal():  # Verifica se o nó atual é o objetivo
            return current_node.get_path(), nodes_searched, math.ceil(current_node.g/0.1), time.time() - start_time  # Retorna o caminho, o número de nós explorados, a profundidade do caminho e o tempo de execução

        for child in current_node.get_children():  # Para cada filho do nó atual
            child.g = current_node.g + 0.1  # Atualiza o valor de g do filho
            child.h = heuristica_final(child.state)  # Calcula o valor de h do filho usando a heurística final
            child.f = child.g + child.h  # Calcula o valor de f do filho

            if child not in open_list and child not in closed_list:  # Verifica se o filho não está na lista de nós abertos e na lista de nós fechados
                open_list.append(child)  # Adiciona o filho à lista de nós abertos
                nodes_searched += 1  # Incrementa o contador de nós explorados

    return None, nodes_searched, None, time.time() - start_time  # Retorna None se não foi encontrado um caminho, o número de nós explorados, profundidade None e o tempo de execução

def main_a_star(matrix1: list):
    start_node = Node(matrix1)  # Cria um nó inicial com a matriz fornecida
    result, nodes_searched, depth, time_spent = a_star(start_node)  # Executa o algoritmo A* a partir do nó inicial

    with open('output.txt', 'a') as f:
        if result is not None:
            for node in result:
                # Imprime cada estado do caminho no arquivo
                print(node.state[0], file=f)
                print(node.state[1], file=f)
                print(node.state[2], file=f)
                print(node.state[3], file=f)
                print(node.state[4], file=f)
                print(node.state[5], file=f)
                print("\n", file=f)  # Adiciona duas linhas em branco
        else:
            # Se nenhum caminho foi encontrado, imprime uma mensagem de erro no arquivo
            print("No solution found.", file=f)
        # Imprime o número do problema e o método usado para resolver no arquivo
        print("Problem number: ",problem, file=f)
        print("Method used to solve: A*", file=f)
        print("\n", file=f)  # Adiciona duas linhas em branco

    with open('estatisticas.txt', 'a') as f:
        # Imprime o número do problema, o número de nós explorados, a profundidade do caminho e o tempo de execução no arquivo
        print(problem, nodes_searched, depth, time_spent, "A*", file=f)

def h_blockers(matrix):
    blockers = 0
    for i in range(lista_de_carros(matrix)[2].coluna + lista_de_carros(matrix)[2].tamanho - 1, BOARD_COLUMNS):# itera todas a colunas a partir da coluna do carro vermelho
        if matrix[lista_de_carros(matrix)[2].linha][i] != ("." or 2): # se encontrar um carro diferente de "." ou 2
            blockers += 1 # incrementa o contador de bloqueadores
    if blockers-1==0:
        return -1000 # se não houver bloqueadores, retorna um valor muito baixo indicando que encontrou a resposta 
    return 3*(blockers -1)   # Retorna a quantidade de bloqueadores no caminho do carro vermelho


def h_distance_to_goal(matrix):
    # Verifica se o carro vermelho já está na coluna 4 (objetivo)
    if lista_de_carros(matrix)[2].coluna == 4:
        return -1000  # Retorna um valor muito baixo indicando que encontrou a resposta
    return (5 - lista_de_carros(matrix)[2].coluna)/3  # Retorna a distância do carro vermelho até o objetivo

def h_available_to_blockers(matrix): #lances disponiveis aos blockers do vermelho (2)
    contador = 0
    for i in range(lista_de_carros(matrix)[2].coluna + lista_de_carros(matrix)[2].tamanho - 1, BOARD_COLUMNS):# itera todas a colunas a partir da coluna do carro vermelho
        if matrix[lista_de_carros(matrix)[2].linha][i] != ("." or 2): # se encontrar um carro diferente de "." ou 2
            num = matrix[lista_de_carros(matrix)[2].linha][i] #guarda a cor do carro
            contador += len(lista_de_carros(matrix)[num].possiveis_coordenadas())#incrementa o contador com o numero de possiveis lances do carro bloqueador
        if 0<=contador<= 3:#return heuristica
            return 0
        return -0.8 
    
def h_camioes_estacionados(matrix): #retorna o numero de camioes "estacionados" na linha 3
    contador = 0
    for carro in lista_de_carros(matrix).values():
        if 14 <= carro.cor <= 17 and carro.linha == 3 and carro.orientacao == "vertical":
            contador += 1
    if contador == 0:#return heuristica
        return 1     
    return 1/contador * 0.1

def heuristica_final(matrix):
    return h_blockers(matrix) + h_distance_to_goal(matrix)+ h_camioes_estacionados(matrix)# + h_available_to_blockers(matrix) nao é utilizado

main_a_star(matrix1)