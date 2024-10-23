# Exercício 1
def define_posicoes(linha, coluna, orientacao, tamanho):
  posição = []
  x = []
  if orientacao == 'vertical':
    i = 0
    while i!=tamanho:
      posição.append([linha, coluna])
      linha +=1
      i+=1
  else:
    i = 0
    while i!=tamanho:
        posição.append([linha, coluna])
        coluna+=1      
        i+=1
  x.append(posição)
  return x

# Exercício 2
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
  if nome_navio in frota:
    position = frota[nome_navio]+define_posicoes(linha, coluna, orientacao, tamanho)
    frota[nome_navio] = position
  else:
    frota[nome_navio] = []
    position = frota[nome_navio]+define_posicoes(linha, coluna, orientacao, tamanho)
    frota[nome_navio] = position
  return frota  

# Exercício 3
def faz_jogada(tabuleiro, linha, coluna):
  if tabuleiro[linha][coluna] == 1:
    tabuleiro[linha][coluna] = 'X'
  else:
    tabuleiro[linha][coluna] = '-'
  return tabuleiro
