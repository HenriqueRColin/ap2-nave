def define_posicoes(linha, coluna, orientacao, tamanho):
  posição = []
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
  return posição
