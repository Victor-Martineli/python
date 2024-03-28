# quando não sabemos quantas variaveis iremos passar em uma função podemos usar os
# *args e **kwargs para facilitar a vida
def teste(arg, *args):
    print('primeiro argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))

teste('python', 'é', 'muito', 'legal')
# *args é utilizado quando não sabemos de antemâo quantos argumentos queremos passar para uma função

# **kwargs permite passar um tamanho variável da palavra-chave dos argumentos parauma função
def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))

minha_funcao(nome='caelum')

# também podemos passar um dicionário acrescido de **, já que se trata de chave e valor
dicionario = {'nome': 'victor', 'idade': 24}
minha_funcao(**dicionario)
