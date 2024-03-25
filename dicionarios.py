# são conjuntos não ordenados que corelaciona uma chave a um  valor

pessoa = {'nome': 'Victor', 'idade': 24, 'cidade': 'Brasília'}
# não é possivel achar um elemento pela posição como em uma lista
# é necessário a chave
print(pessoa['nome'])
print(pessoa['idade'])

# para adicionar um elemento dentro de um dicionário
pessoa['país'] = 'Brasil'
print(pessoa)
# com o metodo keys() podemos ver todas as chaves do dicionário
print(pessoa.keys())
# e com o metodo values() podemos ver os valores
print(pessoa.values())