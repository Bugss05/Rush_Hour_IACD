'''Pesquisa em Profundidade (DFS)'''

from collections import deque
from classes import *
import time
import math
import itertools


problem = int(input("qual é o problema? "))
matrix1= problema(problem)

def dfs(root):
    start_time = time.time()  # Regista o tempo de início da busca
    visited, stack = set(), [Node(root)]  # Conjunto de nós visitados e pilha de nós a serem explorados
    nodes_searched = 0  # Contador de nós explorados
    while stack:
        node = stack.pop()  # Remove o último nó da pilha
        nodes_searched += 1  # Incrementa o contador de nós explorados
        if node.is_goal():  # Verifica se o nó é o objetivo
            path = node.get_path()  # Obtém o caminho até o nó objetivo
            return path, nodes_searched, len(path), time.time() - start_time  # Retorna o caminho, o número de nós explorados, a profundidade do caminho e o tempo de execução
        for child in node.get_children():  # Para cada filho do nó atual
            if child not in visited:  # Se o filho ainda não foi visitado
                visited.add(child)  # Adiciona o filho ao conjunto de nós visitados
                stack.append(child)  # Adiciona o filho à pilha de nós a serem explorados
    return None, nodes_searched, 0, time.time() - start_time  # Retorna None se não foi encontrado um caminho, o número de nós explorados, profundidade 0 e o tempo de execução

def main_dfs(matrix1):
    # Executa a busca em profundidade (DFS) no problema
    result, nodes_searched, depth, time_spent = dfs(matrix1)

    # Abre o arquivo 'output.txt' em modo de escrita e adiciona o resultado da busca
    with open('output.txt', 'a') as f:
        if result is not None:
            # Se um caminho foi encontrado, imprime cada estado do caminho no arquivo
            for node in result:
                print(node.state[0], file=f)
                print(node.state[1], file=f)
                print(node.state[2], file=f)
                print(node.state[3], file=f)
                print(node.state[4], file=f)
                print(node.state[5], file=f)
                print("\n", file=f)
        else:
            # Se nenhum caminho foi encontrado, imprime uma mensagem de erro no arquivo
            print("No solution found.", file=f)
        # Imprime o número do problema e o método usado para resolver no arquivo
        print("Problem number: ",problem, file=f)
        print("Method used to solve: DfS", file=f)
        print("\n", file=f)  # Adiciona duas linhas em branco

    # Abre o arquivo 'estatisticas.txt' em modo de escrita e adiciona as estatísticas da busca
    with open('estatisticas.txt', 'a') as f:
        # Imprime o número do problema, o número de nós explorados, a profundidade do caminho e o tempo de execução no arquivo
        print(problem, nodes_searched, depth, time_spent, "DFS", file=f)  # Adiciona duas linhas em branco

main_dfs(matrix1)