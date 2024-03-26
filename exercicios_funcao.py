def velocidade_media(distancia, tempo):
    velocidade = distancia/tempo
    return ' a velocidade média é {} m/s'.format(velocidade)
print(velocidade_media(100, 20))
print(velocidade_media(150, 22))
print(velocidade_media(200, 30))
print(velocidade_media(50, 3))

def soma_valores(valor1, valor2):
    soma = valor1 + valor2
    return 'a soma é {}'.format(soma)
print(soma_valores(7, 8))

def subtracao_valores(valor1, valor2):
    subtracao = valor1 - valor2
    return 'a subtração é {}'.format(subtracao)
print(subtracao_valores(9, 5))

def calculadora(valor1, valor2):
    soma = valor1 + valor2
    subtracao = valor1 - valor2
    return 'a soma é {} \na subtração é {}'.format(soma, subtracao)

print(calculadora(2, 3))

