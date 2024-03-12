print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')


numero_secreto = 42
total_de_tentativas = 3

#for também pode ser usado para fazer loops
for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa{} de {}'.format(rodada, total_de_tentativas))

    chute = int(input('Advinhe o número: '))
    print('Você digitou: ', chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Você acertou!')
        break
    elif (maior):
        print('Você errou! O seu chute foi maior que o número secreto')
    elif(menor):
        print('Você errou! o seu chute foi menor que o número secreto')


print('Fim do jogo')
