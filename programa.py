from funcoes import *

frota_jogador = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}        

navios = [
    ["porta-aviões", 4, 1],
    ["navio-tanque", 3, 2],
    ["contratorpedeiro", 2, 3],
    ["submarino", 1 ,4],
]     
    
for nome_navio,tamanho,quantidade in navios:
    for i in range(quantidade):
        while True:
            print(f'Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}')
            linha_jogada = int(input('Linha: '))
            coluna_jogada = int(input('coluna: '))
            orientacao = 'vertical'
            if tamanho != 1:
                orientacao_int = int(input("[1] Vertical [2] Horizontal >"))
                if orientacao_int == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota_jogador, linha_jogada, coluna_jogada, orientacao, tamanho):
                break 
            else:
                print('Esta posição não está válida!')
        preenche_frota(frota_jogador, nome_navio, linha_jogada, coluna_jogada, orientacao, tamanho)

print(frota_jogador)