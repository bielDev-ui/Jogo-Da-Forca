import fileHandler as fH
from random import choice
import desenhos as d
def jogar():
    lista_palavras = list()
    arquivo = fH.abrirArquivoLeitura('palavras.txt')
    # 1. VERIFICAÇÃO CRÍTICA: Se for None, para a função aqui mesmo
    if arquivo is None:
        print("Erro: O arquivo não foi carregado corretamente.")
        return #sai da função pra não dar typeError
    print('Bem vindo ao jogo da forca! Arquivo de palavras carregado com sucesso!')
    for linha in arquivo:
        palavra = linha.strip()
        lista_palavras.append(palavra)

    # IMPORTANTE: Fechar o arquivo após ler
    arquivo.close()

    if not lista_palavras:
        print('o arquivo de palavras está vazio')

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
        if not tentativa:
            continue
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