import forca
import advinhacao_final

def jogar():
    print('******************************')
    print('********Menu de jogos*********')
    print('******************************')
    print('1.advinhação')
    print('2.forca')
    escolha = int(input('qual jogo quer jogar? digite o número: '))
    if escolha ==1:
        advinhacao_final.jogar()
    elif escolha == 2:
        forca.jogar()

jogar()