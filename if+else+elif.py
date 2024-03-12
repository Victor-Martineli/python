print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')
#if e else
numero_secreto = 25
#int() transforma uma string em um numeor inteiro
chute = int(input("Advinhe o número: "))


#A identação em python é obrigatória, se não ira considerar como um
#novo comando e não a continuação do mesmo

#if (chute == numero_secreto):
# print("Você acertou")
#else:
#    if (chute > numero_secreto:
#        print("Você errou, seu chute foi maior que o numero secreto")
#    else:
#        print("Você errou, seu chute foi menor que o numero secreto")

#if e else devem ser booleans para fazer a checagem e responder corretamente ao comando

#outra forma melhor de escrever o código é com elif

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto


if (acertou):
    print("Você acertou")
elif (maior):
    print("Você errou, seu chute foi maior que o numero secreto")
elif (menor):
    print("Você errou, seu chute foi menor que o numero secreto")
    
print('fim do jogo')
#desta forma fica melhor de entender o que está acontecendo