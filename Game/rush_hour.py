import pygame
import sys
import os
from classes import *
from matriz_dos_problemas import *
from Todos_os_searchs_problems import *
import time
import math

'''
CÓDIGO DO JOGO DE RUSH HOUR.

Em pygame, ao executar o ficheiro o jogo funciona da seguinte forma:
    seleção entre jogar um nível, deixar a AI jogar um nível, menu de opções

Ao selecionar o menu de opções, encontrará as regras do jogo
Caso selecione jogar um nível, irá escolher um puzzle de 1-79 de acordo com a dificuldade pretendia 
e seguidamente encontra-se pronto a jogar.
Caso selecione AI jogar um nível, irá escolher um puzzle de 1-79 de acordo com a dificuldade pretendia
e seguidamente escolherá o algoritmo que pretende que resolva o puzzle. Esperá um pouco de acordo com a
time complexity e depois aparecerá na sua interface os lances sugeridos pela AI em
'''

def desenhar_grelha(tela):
  """
  Função que desenha a grelha do tabuleiro na tela.

  Argumentos:
    tela: A superfície da tela do Pygame.
  """

  TAMANHO_CELULA = 100
  COR_LINHA = (0, 0, 0)  # Preto

  for i in range(1, 6):
    pygame.draw.line(tela, COR_LINHA, (0, i * TAMANHO_CELULA), (600, i * TAMANHO_CELULA), 2)
  for j in range(1, 6):
    pygame.draw.line(tela, COR_LINHA, (j * TAMANHO_CELULA, 0), (j * TAMANHO_CELULA, 600), 2)

def criar_tabuleiro(matrix):
    """
    Função que cria o tabuleiro inicial do jogo.

    Retorna:
        list: O tabuleiro do jogo (lista de listas de inteiros).
    """
    return matrix

def pintar_veiculos(tela, tabuleiro, cores):

  """
  Função que pinta os veículos no tabuleiro de acordo com seus números.

  Argumentos:
      tela: A superfície da tela do Pygame.
      tabuleiro: O tabuleiro do jogo (lista de listas de inteiros).
      cores: Dicionário que mapeia o número do veículo para sua cor.
  """

  TAMANHO_CELULA = 100
  ESPACO_BORDA = 2  # Espaço entre a borda da célula e o veículo

  for linha in range(6):
    for coluna in range(6):
      numero_veiculo = tabuleiro[linha][coluna] #identificação do número da célula da matriz[linha][coluna
      cor = cores[numero_veiculo] #associação à sua cor
      #cálculo para o desenho do quadrado no tabuleiro
      x = coluna * TAMANHO_CELULA + ESPACO_BORDA
      y = linha * TAMANHO_CELULA + ESPACO_BORDA
      largura = TAMANHO_CELULA - 2 * ESPACO_BORDA
      altura = TAMANHO_CELULA - 2 * ESPACO_BORDA
      #desenho do quadrado
      pygame.draw.rect(tela, cor, (x, y, largura, altura))

def goal_state(tabuleiro):
    #jogo finda se o carro veremlho se encontrar no final da sua linha, ou seja:
    return tabuleiro[2][4] == 2 and tabuleiro[2][5] == 2

def mover_carro( cabeca_y:int , cabeca_x :int, direcao_y :int, direcao_x :int, tamanho:int, distancia:int, matrix:list, carro_selecionado:int, rato_y:int, rato_x:int)->list:
    '''
    Esta função move um carro na matriz. 
    O carro é representado por um número inteiro (carro_selecionado) na matriz.
    '''
    
    # Se o carro move-se para a direita
    if direcao_x > 0 and direcao_y == 0:
        # Enquanto o carro ainda tem comprimento para mover
        while tamanho > 0:
            # Se a posição atual é ocupada pelo carro
            if matrix[rato_y][rato_x] == carro_selecionado:
                # Limpa a posição atual
                matrix[cabeca_y][cabeca_x] = "."
                # Se o carro move-se 1 passo e seu comprimento é 3
                if distancia == 1 and tamanho==3:
                    # Move o carro 2 passos para a direita
                    matrix[rato_y][rato_x + 2] = carro_selecionado
                    # Diminui o comprimento do carro por 3
                    tamanho -= 3
                else:
                    # Move o carro 1 passo para a direita
                    matrix[rato_y][rato_x + 1] = carro_selecionado
                    # Move o cursor 2 passos para a direita
                    rato_x += 2
                    # Diminui o comprimento do carro por 2
                    tamanho -= 2
            else:
                # Limpa a posição atual
                matrix[cabeca_y][cabeca_x] = "."
                # Move o carro 1 passo para a direita
                matrix[rato_y][rato_x] = carro_selecionado
                # Diminui o comprimento do carro por 1
                tamanho -= 1
                # Move o cursor 1 passo para a direita
                rato_x += 1
            # Move a cabeça do carro 1 passo para a direita
            cabeca_x += 1
    # Se o carro move-se para a esquerda
    elif direcao_x < 0 and direcao_y == 0:
        # Enquanto o carro ainda tem comprimento para mover
        while tamanho > 0:
            # Limpa a posição atual
            matrix[cabeca_y][cabeca_x] = "."
            # Move o carro 1 passo para a esquerda
            matrix[rato_y][rato_x] = carro_selecionado
            # Diminui o comprimento do carro por 1
            tamanho -= 1
            # Move o cursor 1 passo para a esquerda
            rato_x += 1
            # Move a cabeça do carro 1 passo para a esquerda
            cabeca_x += 1
    # Se o carro move-se para baixo
    elif direcao_x == 0 and direcao_y > 0:
        # Enquanto o carro ainda tem comprimento para mover
        while tamanho > 0:
            # Se a posição atual é ocupada pelo carro
            if matrix[rato_y][rato_x] == carro_selecionado:
                # Limpa a posição atual
                matrix[cabeca_y][cabeca_x] = "."
                # Se o carro move-se 1 passo e seu comprimento é 3
                if distancia == 1 and tamanho==3:
                    # Move o carro 2 passos para baixo
                    matrix[rato_y+ 2][rato_x ] = carro_selecionado
                    # Diminui o comprimento do carro por 3
                    tamanho -= 3
                else:
                    # Move o carro 1 passo para baixo
                    matrix[rato_y + 1][rato_x] = carro_selecionado
                    # Diminui o comprimento do carro por 2
                    tamanho -= 2
                    # Move o cursor 2 passos para baixo
                    rato_y += 2
            else:
                # Limpa a posição atual
                matrix[cabeca_y][cabeca_x] = "."
                # Move o carro 1 passo para baixo
                matrix[rato_y][rato_x] = carro_selecionado
                # Diminui o comprimento do carro por 1
                tamanho -= 1
                # Move o cursor 1 passo para baixo
                rato_y += 1
            # Move a cabeça do carro 1 passo para baixo
            cabeca_y += 1
    # Se o carro move-se para cima
    elif direcao_x == 0 and direcao_y < 0:
        # Enquanto o carro ainda tem comprimento para mover
        while tamanho > 0:
            # Limpa a posição atual
            matrix[cabeca_y][cabeca_x] = "."
            # Move o carro 1 passo para cima
            matrix[rato_y][rato_x] = carro_selecionado
            # Diminui o comprimento do carro por 1
            tamanho -= 1
            # Move o cursor 1 passo para cima
            rato_y += 1
            # Move a cabeça do carro 1 passo para cima
            cabeca_y += 1
    # Retorna a matriz atualizada
    return matrix

def escolher_nivel(jogador):
    """
    Tela para escolher o nível pretendido
    """
    pygame.init()
    clock = pygame.time.Clock()
    base_font = pygame.font.Font(None, 32)
    input_rect = pygame.Rect(235,400,140,32)
    cor = (0,0,0)
    user_input = ''
    #INICALIZAÇÃO DA TELA
    LARGURA = 600
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    COR_TELA = (255, 255, 255)
    tela.fill(COR_TELA)
    pygame.display.set_caption('Ecolher Puzzle')

    #LOAD DE IMAGENS
    voltar = pygame.image.load('BACK.png').convert_alpha()
    voltar = pygame.transform.scale(voltar, (50, 75)) 
    puzzle = pygame.image.load('PUZZLE.png').convert_alpha()
    puzzle = pygame.transform.scale(puzzle, (600, 250))

    # Criar botões
    voltar = Botao(550, 0, voltar) #botão de voltar ao menu principal

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE: # apagar carateres mal escritos
                    user_input = user_input[:-1]
                elif event.key == pygame.K_RETURN:
                    # Se o Enter for pressionado, termina o input
                    if user_input != '': # não dar erro se input nulo
                        user_input = int(user_input)
                        if user_input > 0 and user_input < 80: # não permitir níveis não existentes
                            if jogador: # oriundo do botão PLAY - ver lógica em função main_menu()
                                play(user_input) #inicialização do jogo
                                dica(user_input) #inicilização da 1ª dica 
                            else: # oriundo do botão AI - ver lógica em função main_menu()
                                ai(user_input)
                        else: 
                            user_input = str(user_input) # caso o input inteiro não seja válido
                    else: pass
                else:
                    # Adiciona o caractere digitado ao input
                    if event.unicode.isdigit():
                        user_input += event.unicode
                    else: pass
        tela.blit(puzzle, (0,0)) # imagem com texto de seleção de níveis
        tela.blit(voltar.image, (550, 0))
        if voltar.draw(tela) == True: # se o botão for clicado
            main_menu()
        
        #atualização da tela para carateres apagados
        tela.fill(COR_TELA)
        tela.blit(puzzle, (0,0))
        tela.blit(voltar.image, (550, 0))
        pygame.draw.rect(tela, cor, input_rect, 2)

        text_surface = base_font.render(user_input, True, (0,0,0))
        tela.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        
        pygame.display.flip()
        clock.tick(60)

def play(user_input):
    """
    Função do jogo em si.
    """
    pygame.init()
    matrix_inicial = problema(user_input) # caso player queira dar reset ao nível
    matrix = copy.deepcopy(matrix_inicial) # guardamos a posição inicial e operamos em matrix
    pygame.display.set_caption('Rush Hour')
    # Tamanho da tela
    LARGURA = 600
    ALTURA = 600
    COR_TELA = (255, 255, 255)
    tela = pygame.display.set_mode((LARGURA, ALTURA))

    #LOAD DE IMAGENS
    voltar = pygame.image.load('BACK.png').convert_alpha()
    voltar = pygame.transform.scale(voltar, (50, 75))
    bola = pygame.image.load('BOLA.png').convert_alpha()
    bola = pygame.transform.scale(bola, (30, 30))
    reset = pygame.image.load('RESET.png').convert_alpha()
    reset = pygame.transform.scale(reset, (50, 50))
    hint = pygame.image.load('HINT.png').convert_alpha()
    hint = pygame.transform.scale(hint, (40, 56))

    # Criação do tabuleiro
    tabuleiro = criar_tabuleiro(matrix)
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    
    # Criar botões
    voltar = Botao(550, 0, voltar) # remeter ao menu principal
    bola = Botao(300, 300, bola) # representação dos lances possíveis
    reset = Botao(10, 10, reset) # voltar ao tabuleiro inicial
    hint = Botao(10, 535, hint) # melhor próximo lance

    # Pintar o tabuleiro
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    pintar_veiculos(tela, tabuleiro, cores)
        
    # Loop principal do jogo
    while True:
        tela.blit(voltar.image, (550, 0))
        if voltar.draw(tela) == True: # se o botão for clicado
            main_menu()
        tela.blit(reset.image, (10, 10))
        if reset.draw(tela) == True: # se o botão for clicado
            play(user_input)
        if hint.draw(tela) == True: # se o botão for clicado
            result = main_a_star(matrix) # algoritmo de pesquisa que resolverá qualquer posição atual
            temp = 0
            for node in result: # todas as posição do path da solução (começa na posição atual)
                temp += 1
                if temp == 2: # seleção da próxima posição
                    matrix = copy.deepcopy(node.state)
                    break
            # Criação do novo tabuleiro
            tabuleiro = criar_tabuleiro(matrix)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            # Pintar o novo tabuleiro
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            pintar_veiculos(tela, tabuleiro, cores)

        rato_x, rato_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #  left click
                    clicada_x = rato_x // 100 # Tamanho da célula = 100
                    clicada_y = rato_y // 100 #  cálculo do indice da célula clicada
                    celula_clicada = (clicada_x, clicada_y)
                    if tabuleiro[celula_clicada[1]][celula_clicada[0]] != '.': # caso não seja espaço vazio
                        carro_selecionado_anterior = -1 # apenas para funcionar na primeira vez que se testar a condição
                        carro_selecionado : int = tabuleiro[celula_clicada[1]][celula_clicada[0]] #store do número associado ao veículo selecionado
                        if carro_selecionado != carro_selecionado_anterior: #objetivo: apenas ter 1 veículo selecionado por vez
                            # repintar o tabuleiro
                            tela.fill(COR_TELA)
                            desenhar_grelha(tela)
                            pintar_veiculos(tela, tabuleiro, cores)
                            lista_lances = lista_de_carros(tabuleiro)[carro_selecionado].possiveis_coordenadas() # lista de tuple(coluna,linha) de todos os lances possíveis de um dado veículo
                            if len(lista_lances) != 0:  # verifica se existem lances possíveis
                                lista_lances_x = []
                                lista_lances_y = []
                                for i in range(len(lista_lances)):
                                    lance_x = lista_lances[i][0] 
                                    lance_y = lista_lances[i][1] 
                                    lance_x = lance_x * 100 + 35 # calculo para colocar a bola representante do lance disponível
                                    lance_y = lance_y * 100 + 35  # calculo para colocar a bola representante do lance disponível
                                    indice_lance_x = lance_x // 100 # atribuição do seu índice
                                    indice_lance_y = lance_y // 100 # atribuição do seu índice
                                    lista_lances_x.append(indice_lance_x) #criação de listas individuais por coordenada
                                    lista_lances_y.append(indice_lance_y) #criação de listas individuais por coordenada
                                    bola.rect.topleft = (lance_x, lance_y) # colocação da bola
                                    tela.blit(bola.image, (lance_x, lance_y)) # colocação da bola
                        carro_selecionado_anterior = carro_selecionado # atualização do carro anterior
                rato_x, rato_y = pygame.mouse.get_pos() # receber os píxeis donde o rato foi pressionado
                rato_x = rato_x // 100 # conversão de píxeis para índice da matrix
                rato_y = rato_y // 100 # conversão de píxeis para índice da matrix
                try:
                    if rato_x in lista_lances_x and rato_y in lista_lances_y: # caso a célula clicada conste como lance possícel
                        cabeca_y = lista_de_carros(tabuleiro)[carro_selecionado].linha # linha da cabeça do carro 
                        cabeca_x = lista_de_carros(tabuleiro)[carro_selecionado].coluna # coluna da cabeça do carro 
                        direcao_y = rato_y - cabeca_y #direção no eixo dos y's do movimento
                        direcao_x = rato_x - cabeca_x #direção no eixo dos x's do movimento
                        tamanho = lista_de_carros(tabuleiro)[carro_selecionado].tamanho # tamanho do veículo
                        distancia = abs(direcao_x) + abs(direcao_y) # módulo da distância do movimento (diferente da direção que pode ser negativa)
                        mover_carro(cabeca_y, cabeca_x, direcao_y, direcao_x, tamanho, distancia, tabuleiro, carro_selecionado, rato_y, rato_x) #mover o carro para a célula clicada
                        # pintar novo tabuleiro com o carro já movido
                        tabuleiro = criar_tabuleiro(matrix)
                        pintar_veiculos(tela, tabuleiro, cores)
                except: # para puder selcionar outras casas sem ser uma com bola e não dar erro
                    pass                  
        # Verificação se o jogo terminou
        if goal_state(tabuleiro):
            win()
        pygame.display.update()

def win():
    """
    Função para a tela de vitória.
    """
    # Inicialização da tela 

    LARGURA = 600
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Vitória')
    win = pygame.image.load('VITORIA.png').convert_alpha()
    win = pygame.transform.scale(win, (600, 600))
    voltar = pygame.image.load('BACK.png').convert_alpha()
    voltar = pygame.transform.scale(voltar, (50, 75))
        
    # Criar botões
    voltar = Botao(550, 0, voltar) # botão para remeter para o menu_principal

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        tela.blit(win, (0, 0))
        tela.blit(voltar.image, (550, 0))
        pygame.display.update()
        if voltar.draw(tela) == True: # se o botão for clicado
            main_menu()
        
def opcoes_menu():
    # Tela
    LARGURA = 600
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    
    #LOAD IMAGENS
    pygame.display.set_caption('Opções')
    opcoes = pygame.image.load('OPÇOES_MENU.png').convert_alpha()
    opcoes = pygame.transform.scale(opcoes, (600, 600))
    voltar = pygame.image.load('BACK.png').convert_alpha()
    voltar = pygame.transform.scale(voltar, (50, 75))
        
    # Criar botões
    voltar = Botao(550, 0, voltar)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        tela.blit(opcoes, (0, 0))
        tela.blit(voltar.image, (550, 0))
        if voltar.draw(tela) == True: #se for clicado ir para menu principal
            main_menu()
        pygame.display.update()

def ai(user_input):
    
    '''
    
    Função responsável pela tela de selação do algoritmo de pesquisa a aplicar na
    resolução do nível previamente selecionado
    
    '''
    # Tela
    LARGURA = 600
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    COR_TELA = (255, 255, 255)
    tela.fill(COR_TELA)
    pygame.display.set_caption('AI Play')

    # Carregar Imagens
    imagem_bfs = pygame.image.load('BFS.png').convert_alpha()
    imagem_bfs = pygame.transform.scale(imagem_bfs, (200, 100))
    imagem_dfs = pygame.image.load('DFS.png').convert_alpha()
    imagem_dfs = pygame.transform.scale(imagem_dfs, (200, 100))
    imagem_astar = pygame.image.load('ASTAR.png').convert_alpha()
    imagem_astar = pygame.transform.scale(imagem_astar, (200, 100))
    imagem_ids = pygame.image.load('IDS.png').convert_alpha()
    imagem_ids = pygame.transform.scale(imagem_ids, (200, 100))
    voltar = pygame.image.load('BACK.png').convert_alpha()
    voltar = pygame.transform.scale(voltar, (50, 75))
    robot = pygame.image.load('ROBOT.webp').convert_alpha()
    robot = pygame.transform.scale(robot, (200, 200))

    #inicilizar botões
    imagem_astar = Botao(310, 385, imagem_astar) # botão A*
    imagem_bfs = Botao(90, 240, imagem_bfs) # botão BFS
    imagem_dfs = Botao(310, 240, imagem_dfs) # botão DFS
    imagem_ids = Botao(90, 385, imagem_ids) # botão IDS
    voltar = Botao(550, 0, voltar) # botão para voltar para o menu principal

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        tela.blit(robot, (210, 20))
        if imagem_ids.draw(tela) == True: #se o botão for clicado, aplicar a função ids
            ids(user_input)
        if imagem_bfs.draw(tela) == True: #se o botão for clicado, aplicar a função bfs
            bfs(user_input)
        if imagem_dfs.draw(tela) == True: #se o botão for clicado, aplicar a função dfs
            dfs(user_input)
        if imagem_astar.draw(tela) == True: #se o botão for clicado, aplicar a função A*
            a_star(user_input)
        tela.blit(voltar.image, (550, 0))
        if voltar.draw(tela) == True: #se o botão for clicado, voltar para o menu principal
            main_menu()
        pygame.display.update()

def a_star(user_input): 
    # Tela
    pygame.init()
    matrix_inicial = problema(user_input)
    matrix = copy.deepcopy(matrix_inicial)
    pygame.display.set_caption('A* Player')
    problem = 35
    
    # Tamanho da tela
    LARGURA = 600
    ALTURA = 600
    COR_TELA = (255, 255, 255)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    
    # Criação do tabuleiro
    tabuleiro = criar_tabuleiro(matrix)
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    
    # Pintar o tabuleiro
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    pintar_veiculos(tela, tabuleiro, cores)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        result = main_a_star(matrix) # path de matrizes até ao goal state
        for node in result:
            matrix = copy.deepcopy(node.state) # tornar cada nó do grafo da path numa matriz usável neste programa
            #Incializaçao da tela e o tabuleiro uma matrix associada a cada nó da path 
            tabuleiro = criar_tabuleiro(matrix)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            pintar_veiculos(tela, tabuleiro, cores)
            pygame.display.update()
            time.sleep(0.7) # pequeno delay entre cada representação no tabuleiro do nó do grafo
            if goal_state(tabuleiro):
                time.sleep(1) # pequeno delay para ver o tabuleiro resolvido
                win()

def bfs(user_input): 
    # Tela
    pygame.init()
    matrix_inicial = problema(user_input)
    matrix = copy.deepcopy(matrix_inicial)
    pygame.display.set_caption('BFS Player')
    problem = 35
    
    # Tamanho da tela
    LARGURA = 600
    ALTURA = 600
    COR_TELA = (255, 255, 255)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    
    # Criação do tabuleiro
    tabuleiro = criar_tabuleiro(matrix)
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    
    # Pintar o tabuleiro
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    pintar_veiculos(tela, tabuleiro, cores)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        result = main_bfs(matrix) # path de matrizes até ao goal state
        for node in result:
            matrix = copy.deepcopy(node.state) # tornar cada nó do grafo da path numa matriz usável neste programa
            #Incializaçao da tela e o tabuleiro uma matrix associada a cada nó da path 
            tabuleiro = criar_tabuleiro(matrix)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            pintar_veiculos(tela, tabuleiro, cores)
            pygame.display.update()
            time.sleep(0.7) # pequeno delay entre cada representação no tabuleiro do nó do grafo
            if goal_state(tabuleiro):
                time.sleep(1) # pequeno delay para ver o tabuleiro resolvido
                win()
            
def dfs(user_input): 
    # Tela
    pygame.init()
    matrix_inicial = problema(user_input)
    matrix = copy.deepcopy(matrix_inicial)
    pygame.display.set_caption('DFS Player')
    problem = 35
    
    # Tamanho da tela
    LARGURA = 600
    ALTURA = 600
    COR_TELA = (255, 255, 255)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    
    # Criação do tabuleiro
    tabuleiro = criar_tabuleiro(matrix)
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    
    # Pintar o tabuleiro
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    pintar_veiculos(tela, tabuleiro, cores)

    #BOTAO BACK
    voltar = pygame.image.load('BACK.png').convert_alpha()
    voltar = pygame.transform.scale(voltar, (50, 75))
    voltar = Botao(550, 0, voltar)

    #TEMPO
    contador_tempo1 = 0
    contador_tempo2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        result = main_dfs(matrix) # path da de matrizes da solução
        for node in result:
            contador_tempo1 += 1
            matrix = copy.deepcopy(node.state) # tornar cada nó operacional neste programa indexando à variável matrix
            tabuleiro = criar_tabuleiro(matrix)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            pintar_veiculos(tela, tabuleiro, cores)
            pygame.display.update()
            if contador_tempo1 > 10:
                contador_tempo2 += 0.5
                time.sleep(1/(math.e ** (contador_tempo2/10))) # à medida que o número de nós aumenta, na UI o tempo entre eles diminiu exponencialmente
            else:
                contador_tempo1 += 1 
                time.sleep(0.7)
            if goal_state(tabuleiro):
                time.sleep(1)
                win()   

def ids(user_input): 
    # Tela
    pygame.init()
    matrix_inicial = problema(user_input)
    matrix = copy.deepcopy(matrix_inicial)
    pygame.display.set_caption('IDS Player')
    problem = 35
    
    # Tamanho da tela
    LARGURA = 600
    ALTURA = 600
    COR_TELA = (255, 255, 255)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    
    # Criação do tabuleiro
    tabuleiro = criar_tabuleiro(matrix)
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    
    # Pintar o tabuleiro
    tela.fill(COR_TELA)
    desenhar_grelha(tela)
    pintar_veiculos(tela, tabuleiro, cores)

    #BOTAO BACK
    voltar = pygame.image.load('BACK.png').convert_alpha()
    voltar = pygame.transform.scale(voltar, (50, 75))
    voltar = Botao(550, 0, voltar)

    #TEMPO
    contador_tempo1 = 0
    contador_tempo2 = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        result = main_ids(matrix) # path da de matrizes da solução
        for node in result:
            contador_tempo1 += 1
            matrix = copy.deepcopy(node.state) # tornar cada nó operacional neste programa indexando à variável matrix
            tabuleiro = criar_tabuleiro(matrix)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            tela.fill(COR_TELA)
            desenhar_grelha(tela)
            pintar_veiculos(tela, tabuleiro, cores)
            pygame.display.update()
            if contador_tempo1 > 10:
                contador_tempo2 += 0.5
                time.sleep(1/(math.e ** (contador_tempo2/10))) # à medida que o número de nós aumenta, na UI o tempo entre eles diminiu exponencialmente
            else:
                contador_tempo1 += 1 
                time.sleep(0.7)
            if goal_state(tabuleiro):
                time.sleep(1)
                win()   

def main_menu():
    # Inicialização da Tela
    LARGURA = 600
    ALTURA = 600
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption('Main Menu')
    
    # Carregar imagens
    menu = pygame.image.load('MENU.png').convert_alpha()
    menu = pygame.transform.scale(menu, (LARGURA, ALTURA))
    jogar = pygame.image.load('PLAY.png').convert_alpha()
    jogar = pygame.transform.scale(jogar, (200, 100))
    opcoes = pygame.image.load('OPTIONS.png').convert_alpha()
    opcoes = pygame.transform.scale(opcoes, (200, 100))
    ai_play = pygame.image.load('AIPLAY.png').convert_alpha()
    ai_play = pygame.transform.scale(ai_play, (200, 100))

    # Criar botões
    jogar = Botao(200, 125, jogar) # botão PLAY
    ai_play = Botao(200, 250, ai_play) # botão AI
    opcoes = Botao(200, 375, opcoes) # botão OPTIONS

    while True:
        tela.blit(menu, (0, 0))
        '''
        VARIÁVEL JOGADOR: para evitar fazer funções de escolha de nível diferentes para
        caso seja para o jogador jogar ou a AI jogar, cria-se a variavél JOGADOR com o objetivo
        de funcionar como um interrupetor: caso esteja ligado(TRUE), o programa na função
        escolher_nivel() irá executar o bloco de comandos para que seja possível o jogador jogar.
        Caso o interrupetor esteja desligado (False), o programa executará o bloco remetente à AI jogar.
        '''
        if jogar.draw(tela) == True: #se PLAY clicado 
            jogador = True
            escolher_nivel(jogador)
        if opcoes.draw(tela) == True: #se OPTIONS clicado 
            opcoes_menu()
        if ai_play.draw(tela) == True: #se AI clicado
            jogador = False
            escolher_nivel(jogador)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

main_menu() #chamar a função main_menu()