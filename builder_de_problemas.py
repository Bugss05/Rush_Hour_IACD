'''este script serve como uma ferramenta para criar problemas de tabuleiro personalizados para posterior resolução ou análise.'''

# Matriz que representa o tabuleiro do problema
matrix = [
    [".",".",".",".",".",".",],
    [".",".",".",".",".",".",],
    [".",".",".",".",".",".",],
    [".",".",".",".",".",".",],
    [".",".",".",".",".",".",],
    [".",".",".",".",".",".",],
]

# Solicita ao usuário o número do problema e a quantidade de carros
problema = int(input("qual é o problema? "))
quantos_carros = int(input("quantos carros? "))

# Loop para adicionar os carros na matriz
while quantos_carros > 0:
    # Solicita ao usuário a posição, orientação e cor do carro
    x = int(input("qual é a posição x? "))
    y = int(input("qual é a posição y? "))
    orientacao = int(input("qual é a orientação (0=H)? "))
    cor = int(input("qual é a cor? "))

    # Define o tamanho do carro com base na cor
    if cor < 14 and cor >= 0:
        tamanho = 2
    else:
        tamanho = 3

    # Loop para adicionar as partes do carro na matriz
    while tamanho > 0:
        try:
            # Verifica se a posição está ocupada ou fora de alcance
            if matrix[y][x] != ".":
                raise ValueError("Posição ocupada ou fora de alcance")
            
            # Adiciona a cor do carro na posição da matriz
            matrix[y][x] = cor

            # Move a posição do carro de acordo com a orientação
            if orientacao == 0:
                x += 1
                tamanho -= 1
            else:
                y += 1
                tamanho -= 1
        except:
            raise ValueError("Posição ocupada ou fora de alcance")

    # Decrementa a quantidade de carros restantes
    quantos_carros -= 1

# Abre o arquivo 'problemas.txt' em modo de escrita e adiciona o problema e a matriz
with open('problemas.txt', 'a') as f:
    print(problema, file=f)
    print("[", file=f)
    for row in matrix:
        print(' '.join(str(x) for x in row), file=f)
    print("]", file=f)
    print("\n", file=f)
    print("\n", file=f)