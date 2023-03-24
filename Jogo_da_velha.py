
from sys import exit


def imprimir_jogo(matriz_game):
    cont = 0
    global matriz2
    for elemento_game in matriz_game:
        print(' | '.join(elemento_game).replace("'", ''))
        if cont < 2 and matriz_game is not matriz2:
            print('----------')
            cont += 1
        elif cont < 2:
            print('----------------------------')
            cont += 1


def jogada(matriz1, matriz2_g, escolha):
    global linha, coluna
    flag = 0
    if escolha == 1:
        simbolo = 'X'
    else:
        simbolo = '0'

    while flag == 0:
        coluna = int(input('Digite a coluna que você quer jogar:\n'
                           'c: '))
        linha = int(input('Digite a linha que você quer jogar:\n'
                          'l: '))
        if matriz1[linha][coluna] == 'X' or matriz1[linha][coluna] == '0':
            print('Coluna x Linha ocupada: escolha outra')
        else:
            flag = 1

    matriz1[linha][coluna] = simbolo
    matriz2_g[linha][coluna] = "   " + simbolo + "   "

    return matriz1, matriz2_g


def check(lista):
    flag2, flag3, flag4, flag5, flag6, flag7, flag8, flag9 = 0, 0, 0, 0, 0, 0, 0, 0
    if matriz[0][0] == 'X':
        if matriz[0][1] == 'X':
            if matriz[0][2] == 'X':
                flag2 = 1
        elif matriz[1][0] == 'X':
            if matriz[2][0] == 'X':
                flag3 = 1
        elif matriz[1][1] == 'X':
            if matriz[2][2] == 'X':
                flag4 = 1
    elif matriz[0][1] == 'X':
        if matriz[1][1] == 'X':
            if matriz[2][1] == 'X':
                flag5 = 1
    elif matriz[0][2] == 'X':
        if matriz[1][2] == 'X':
            if matriz[2][2] == 'X':
                flag6 = 1
        elif matriz[1][1] == 'X':
            if matriz[2][0] == 'X':
                flag7 = 1
    elif matriz[1][0] == 'X':
        if matriz[1][1] == 'X':
            if matriz[2][1] == 'X':
                flag8 = 1
    elif matriz[2][0] == 'X':
        if matriz[2][1] == 'X':
            if matriz[2][2] == 'X':
                flag9 = 1

    if matriz[0][0] == '0':
        if matriz[0][1] == '0':
            if matriz[0][2] == '0':
                flag2 = 1
        elif matriz[1][0] == '0':
            if matriz[2][0] == '0':
                flag3 = 1
        elif matriz[1][1] == '0':
            if matriz[2][2] == '0':
                flag4 = 1
    elif matriz[0][1] == '0':
        if matriz[1][1] == '0':
            if matriz[2][1] == '0':
                flag5 = 1
    elif matriz[0][2] == '0':
        if matriz[1][2] == '0':
            if matriz[2][2] == '0':
                flag6 = 1
        elif matriz[1][1] == '0':
            if matriz[2][0] == '0':
                flag7 = 1
    elif matriz[1][0] == '0':
        if matriz[1][1] == '0':
            if matriz[2][1] == '0':
                flag8 = 1
    elif matriz[2][0] == '0':
        if matriz[2][1] == '0':
            if matriz[2][2] == '0':
                flag9 = 1
    lista.append(flag2)
    lista.append(flag3)
    lista.append(flag4)
    lista.append(flag5)
    lista.append(flag6)
    lista.append(flag7)
    lista.append(flag8)
    lista.append(flag9)

    return lista


def comecar_jogo(cont_cj, flag_ganhador_x_cj, flag_empate_cj, flag_ganhador_0_cj, matriz_cj, matriz2_cj, lista_flags_cj):
    player_choice = int(input('Escolha X ou 0\n'
                              'Digite 1 para "X" e Digite 2 para "0": '))

    if player_choice == 1:
        player_choice2 = 2
    else:
        player_choice2 = 1

    print('VAMOS COMEÇAR!')
    while 0 == 0:
        cont_cj += 1
        imprimir_jogo(matriz_cj)
        print('\n')
        imprimir_jogo(matriz2_cj)
        print('\n')
        print('Jogador 1:\n')
        jogada(matriz_cj, matriz2_cj, player_choice)
        print('\n')
        check(lista_flags_cj)
        for elemento in lista_flags_cj:
            if elemento == 1:
                flag_ganhador_x_cj = 1
            elif cont_cj > 9:
                flag_empate_cj = 1
        if flag_ganhador_x_cj == 1 or flag_empate_cj == 1:
            break

        imprimir_jogo(matriz_cj)
        print('\n')
        imprimir_jogo(matriz2_cj)
        print('\n')
        print('Jogador 2:\n')
        jogada(matriz_cj, matriz2_cj, player_choice2)
        print('\n')
        check(lista_flags_cj)
        for elemento in lista_flags_cj:
            if elemento == 1:
                flag_ganhador_0_cj = 1
            elif cont_cj > 9:
                flag_empate_cj = 1
        if flag_ganhador_0_cj == 1 or flag_empate_cj == 1:
            break
        cont_cj += 1
        lista_flags_cj = []

    if flag_ganhador_x_cj == 1:
        print('Jogador 1 vence')
        imprimir_jogo(matriz_cj)
        jogar_novamente()
    elif flag_ganhador_0_cj == 1:
        print('Jogador 2 vence')
        imprimir_jogo(matriz_cj)
        jogar_novamente()
    else:
        print('empate')
        imprimir_jogo(matriz_cj)
        jogar_novamente()


def jogar_novamente():
    escolha_jn = input('Quer jogar novamente?\nDigite sim para jogar novamente e não para sair')
    if escolha_jn == 'sim':
        zerador_de_variaveis()
    else:
        exit(1)


def zerador_de_variaveis():
    global cont, flag_ganhador_x, flag_empate, flag_ganhador_0, matriz, matriz2, lista_flags
    cont = 0
    flag_ganhador_x = 0
    flag_empate = 0
    flag_ganhador_0 = 0
    matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    matriz2 = [['c:0 l:0', 'c:1 l:0', 'c:2 l:0'], ['c:0 l:1', 'c:1 l:1', 'c:2 l:1'], ['c:0 l:2', 'c:1 l:2', 'c:2 l:2']]
    lista_flags = []

    comecar_jogo(cont, flag_ganhador_x, flag_empate, flag_ganhador_0, matriz, matriz2, lista_flags)


coluna = 0
linha = 0
cont = 0
flag_ganhador_x = 0
flag_empate = 0
flag_ganhador_0 = 0
matriz = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
matriz2 = [['c:0 l:0', 'c:1 l:0', 'c:2 l:0'], ['c:0 l:1', 'c:1 l:1', 'c:2 l:1'], ['c:0 l:2', 'c:1 l:2', 'c:2 l:2']]
lista_flags = []

comecar_jogo(cont, flag_ganhador_x, flag_empate, flag_ganhador_0, matriz, matriz2, lista_flags)
