import jogo as j
import fileHandler as fH




def mostrar_menu():
    print("="*30)
    print(' ' * 7 + 'JOGO DA FORCA')
    print('='*30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print(' 3 - SAIR\n')
    print('='*30)

arquivo = 'score.txt'
if fH.existeArquivo(arquivo):
    print('arquivo localizado no PC')
else:
    print('ARQUIVO NÃO EXISTE.')
    fH.criaArquivo(arquivo)

while True:
    mostrar_menu()
    opcao = int(input('Escolha a opção (1/2/3): '))

    if opcao == 1:
        print('iniciar jogo!')
        j.jogar()
    elif opcao == 2:
        print('score!')
        dados = fH.listarArquivo('score.txt')
        if not dados:
            print('score vazio')
        else:
            i = 1
            for jogador in dados:
                print(f'{i} -> {jogador[0]}, pontuação: {jogador[5].strip()}')
                i += 1
    elif opcao == 3:
        print('Saindo do jogo. Até mais!')
        break
    else:
        print('opção inválida.')


