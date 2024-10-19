def define_posicoes(linha, coluna, orientacao, tamanho):
  posição = []
  if orientacao == 'vertical':
    i = 0
    while i!=tamanho:
      linha +=1
      posição.append([linha, coluna])
      i+=1
  else:
    i = 0
    while i!=tamanho:
      coluna +=1
      posição.append([linha, coluna])
      i+=1
  return posição
