import fileHandler as fH
from random import choice
import desenhos as d
def jogar():
    lista_palavras = list()
    arquivo = fH.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    palavra_sorteada = choice(lista_palavras)


    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        #CONDIÇÃO DE VITÓRIA
        if adivinha == palavra_sorteada:
            print('você acertou!')
            break

        #TENTATIVAS
        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('você já usou esta letra!')
            continue
        else:
            digitadas += tentativa #ou append
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1 
                print('Você errou!')
        
        score = d.desenhar_forca(erros)

        #CONDIÇÃO DE FIM DE JOGO
        if erros == 6:
            print('ENFORCADO!')  
            print(f'a palavra sorteada era {palavra_sorteada}.')
            break

        fH.inserir_score('score.txt', nome, score)
    for x in range(50):
        print()