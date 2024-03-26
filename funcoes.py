# usando o comando def podemops definir uma função generica
def velocidade(espaco, tempo):
    v = espaco/tempo
    return v

print(velocidade(100, 20))
# para que uma função possa usar de outra é necessário que ela de um return

aceleracao = velocidade(100, 20)/20
print(aceleracao)

def dados(nome, idade=None):
    if idade is not None:
        return 'nome: {} \nidade: {}'.format(nome, idade)
    else:
        return 'nome: {} \nidade: não informada'.format(nome)

print(dados('Victor', 24))

def calculadora(x, y):
    return {'soma': x+y, 'subtração': x-y}

resultados = calculadora(1, 2)
for key in resultados:
    print('{} = {}'.format(key, resultados[key]))
