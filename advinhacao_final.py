print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 42
pontuacao_inicial = 1000
nivel = int(input('selecione entre o nivel 1, 2 ou 3: '))

if nivel == 1:
    tentativas = 20
    penalidade = 50

elif nivel == 2:
    tentativas = 10
    penalidade = 100

elif nivel == 3:
    tentativas = 5
    penalidade = 200

print('Você selecionou o nivel {}, possui {} tentativas e {} pontos'.format(nivel, tentativas, pontuacao_inicial))


pontos_restantes = pontuacao_inicial - penalidade

for rodada in range(1, tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, tentativas))

    chute = int(input('Advinhe o número: '))
    print('Você digitou: ', chute)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou!')
        break

    elif maior:
        print('Você errou! O seu chute foi maior que o número secreto, pontos restantes: {}'.format(pontos_restantes))
    elif menor:
        print('Você errou! o seu chute foi menor que o número secreto, pontos restantes: {}'.format(pontos_restantes))
    pontos_restantes = pontos_restantes - penalidade

print('Fim do jogo')
