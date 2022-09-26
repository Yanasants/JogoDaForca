import random
from artes import fases, vencedor
from palavras import *

repete_jogo = True
while (repete_jogo==True):
    fim_de_jogo = False
    vidas = len(fases) - 1

    print('\n\n')
    boas_vindas = ' BEM VINDOS! JOGO DA FORCA - EDIÇÃO: DIVERSIDADE TECH '
    print("{frase:#^150}".format(frase = boas_vindas))

    categoria_escolhida = input("\n\nEscolha uma categoria: 'animais', 'frutas', 'objetos' ou 'profissoes': ").lower()
    categorias_dict = {'animais': animais_separados, 'frutas': frutas_separadas, 'objetos': objetos_separados, 'profissoes': profissoes_separadas}
    categorias_corrigido_dict = {'animais': animais_corrigido, 'frutas': frutas_corrigido, 'objetos': objetos_corrigido, 'profissoes': profissoes_corrigido}

    while (categoria_escolhida not in categorias_dict.keys()):
        print('Categoria inválida! Tente novamente.')
        categoria_escolhida = input("Escolha uma categoria: 'animais', 'frutas', 'objetos' ou 'profissoes': ").lower()

    palavra_escolhida = random.choice(categorias_corrigido_dict[categoria_escolhida])

    comprimento_palavra = len(palavra_escolhida)
    letras_usadas = []
    display = []

    for espaco in range(comprimento_palavra):
        display += "_"

    while not fim_de_jogo:
        print(fases[vidas])
        print(f"{' '.join(display)}")
        print('__'*30)
        letra_adivinhada = input("\nEscolha uma letra: ").lower()

        while (letra_adivinhada in letras_usadas):
            print(f"\nVocê já escolheu a letra '{letra_adivinhada}'. Tente novamente.")
            letra_adivinhada = input("Escolha uma letra: ").lower()

        letras_usadas.append(letra_adivinhada)

        for posicao in range(comprimento_palavra):
            letra = palavra_escolhida[posicao]
            if letra == letra_adivinhada:
                display[posicao] = letra
        
        if (letra_adivinhada not in palavra_escolhida):
            vidas -= 1
            if (vidas != 0):
                print(f"\nVocê escolheu a letra '{letra_adivinhada}', que não está na palavra. Perdeu uma vida! Restam apenas {vidas} tentativa(s).")
            else:
                fim_de_jogo = True
                index = categorias_corrigido_dict[categoria_escolhida].index(palavra_escolhida)
                print(fases[0])
                print(f"\nVocê perdeu! A palavra a ser adivinhada era {categorias_dict[categoria_escolhida][index]}.\n")
                continua = input('\nDeseja jogar novamente? (s/n)')
                while (continua != 's' and continua != 'n'):
                    print('Resposta inválida. Digite novamente.')
                    continua = input('\nDeseja jogar novamente? (s/n)')
                if (continua=='n'):
                    repete_jogo = False

        if not "_" in display:
            fim_de_jogo = True
            print("\nParabéns! Você venceu!")
            print(vencedor)
            continua = input('\nDeseja jogar novamente? (s/n)')
            while (continua != 's' and continua != 'n'):
                print('Resposta inválida. Digite novamente.')
                continua = input('\nDeseja jogar novamente? (s/n)')
                if (continua=='n'):
                    repete_jogo =  False