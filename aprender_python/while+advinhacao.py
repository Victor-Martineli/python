print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 25
total_de_tentaivas = 3
rodada = 1
#while

while(rodada <= total_de_tentaivas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentaivas))
    #para contabilizar as rodadas vamos adicionar sempre mais um no fim do elif
    chute = int(input("Advinhe o número: "))
    print('Você digitou: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if (acertou):
        print("Você acertou")
        break
    elif (maior):
        print("Você errou, seu chute foi maior que o numero secreto")
    elif (menor):
        print("Você errou, seu chute foi menor que o numero secreto")
        
    rodada = rodada + 1
        
print('fim do jogo')
