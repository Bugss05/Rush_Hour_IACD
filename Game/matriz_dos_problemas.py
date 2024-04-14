'''este script serve como uma interface para acessar problemas específicos e suas matrizes correspondentes a partir de um arquivo de texto.'''

import random

# Função que recebe o nome do arquivo como parâmetro
def parse_problems(filename):
    # Abre o arquivo no modo de leitura
    with open(filename, 'r') as f:
        # Lê todas as linhas do arquivo e cria um iterador
        lines = iter(f.readlines())
        # Cria um dicionário para armazenar os problemas
        problems = {}
        # Itera sobre cada linha do arquivo
        for line in lines:
            # Remove espaços em branco do início e fim da linha
            line = line.strip()
            # Verifica se a linha contém apenas dígitos
            if line.isdigit():
                # Converte a linha para um número inteiro
                problem_number = int(line)
                # Pula a próxima linha que contém '['
                next(lines)
                # Cria uma lista vazia para armazenar a matriz do problema
                matrix = []
                # Loop infinito para ler as linhas da matriz
                while True:
                    # Lê a próxima linha e remove espaços em branco
                    matrix_line = next(lines).strip()
                    # Verifica se a linha é igual a ']'
                    if matrix_line == ']':
                        # Sai do loop se encontrar ']'
                        break
                    # Divide a linha em elementos separados por espaços
                    # Converte os elementos para inteiros se forem dígitos, caso contrário, mantém como '.'
                    matrix.append([int(i) if i.isdigit() else '.' for i in matrix_line.split()])
                # Armazena a matriz do problema no dicionário
                problems[problem_number] = matrix
        # Retorna o dicionário com os problemas
        return problems

# Função que recebe o número do problema como parâmetro
def get_problem_matrix(problem_number):
    # Chama a função parse_problems para obter um dicionário com os problemas
    problems = parse_problems('problemas.txt')
    # Verifica se o número do problema está presente no dicionário
    if problem_number in problems:
        # Imprime o número do problema
        print(f"Problem number: {problem_number}")
        # Retorna a matriz do problema correspondente
        return problems[problem_number]
    else:
        # Retorna None se o número do problema não for encontrado
        return None

# Examp
def problema (problema:int): 
    return get_problem_matrix(problema)

