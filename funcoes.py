def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes 

# Exercício 2
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    nova_posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(nova_posicao)
    else:
        frota[nome_navio] = [nova_posicao]

    return frota


# Exercício 3
def faz_jogada(tabuleiro, linha, coluna):
  if tabuleiro[linha][coluna] == 1:
    tabuleiro[linha][coluna] = 'X'
  else:
    tabuleiro[linha][coluna] = '-'
  return tabuleiro

# Exercício 4
def posiciona_frota(frota):
    # Inicializa um tabuleiro 10x10 com 0s
    grid = [[0 for _ in range(10)] for _ in range(10)]
    
    # Percorre o dicionário de navios
    for navio, posicoes in frota.items():
        for posicao in posicoes:
            for coordenada in posicao:
                x, y = coordenada
                # Preenche o grid com 1 onde há navios
                grid[x][y] = 1
                
    return grid

# Exercício 5
def afundados(frota, tabuleiro):
    mortos = 0
    for chave, valor in frota.items():
        for i in valor:
            lista_posicoes_mortas = []
            for j in i:
                x, y = j
                if tabuleiro[x][y] == 'X':
                    lista_posicoes_mortas.append(j)
                    if i == lista_posicoes_mortas:
                        mortos +=1
                else:
                    continue
    return mortos
  
# Exercício 6
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    for linha, coluna in posicoes_navio:
        if linha < 0 or linha >= 10 or coluna < 0 or coluna >= 10:
            return False
        
    for navio, lista_posicoes in frota.items():
        for posicoes in lista_posicoes:
            for pos in posicoes:
                if pos in posicoes_navio:
                    return False

    return True
