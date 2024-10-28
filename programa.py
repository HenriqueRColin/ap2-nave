from funcoes import *


frota_oponente = {
    'porta-aviões': [[[9, 1], [9, 2], [9, 3], [9, 4]]],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

frota_jogador = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": []
}


navios = [
    ["porta-aviões", 4, 1],
    ["navio-tanque", 3, 2],
    ["contratorpedeiro", 2, 3],
    ["submarino", 1, 4]
]

for nome_navio, tamanho, quantidade in navios:
    for _ in range(quantidade):
        while True:
            print(f'Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}')
            linha_jogada = int(input('Linha: '))
            coluna_jogada = int(input('Coluna: '))
            orientacao = 'vertical'
            if tamanho != 1:
                orientacao_int = int(input("[1] Vertical [2] Horizontal > "))
                orientacao = "vertical" if orientacao_int == 1 else "horizontal"
            if posicao_valida(frota_jogador, linha_jogada, coluna_jogada, orientacao, tamanho):
                preenche_frota(frota_jogador, nome_navio, linha_jogada, coluna_jogada, orientacao, tamanho)
                break
            else:
                print('Esta posição não está válida!')


tabuleiro_jogador = posiciona_frota(frota_jogador)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True
posicoes_atacadas = set()

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    while True:
        linha = int(input("Escolha a linha (0-9) para atacar: "))
        if 0 <= linha <= 9:
            break
        print("Linha inválida!")


    while True:
        coluna = int(input("Escolha a coluna (0-9) para atacar: "))
        if 0 <= coluna <= 9:
            break
        print("Coluna inválida!")

    if (linha, coluna) in posicoes_atacadas:
        print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        continue
    posicoes_atacadas.add((linha, coluna))


    faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente):
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
