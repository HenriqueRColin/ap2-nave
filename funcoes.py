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

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
  frota_update = {}
  position = define_posicoes(linha, coluna, orientacao, tamanho)
  frota_update[nome_navio] = frota[nome_navio]
  frota_update[nome_navio] += position
  return frota_update
