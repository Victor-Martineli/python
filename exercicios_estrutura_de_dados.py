lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
maior_valor = lista[0]
menor_valor = lista[0]
pares = []
ocorrencias_item1 = 0
media_elementos = 0
soma_negativos = 0

for index in range(0, len(lista)):
    # o loop for vai verificar cada elemento dentro de "lista" e comparar com "maior_valor"
    # caso o valor de "maior_valor" seja menor que de lista ele o subistitui e compara com o próximo valor
    # assim sucessivamente, até ficar com o maior valor possivel dentro de lista
    if maior_valor < lista[index]:
        maior_valor = lista[index]
    # mesma lógica do anterior porem agora buscando o menor valor
    if menor_valor > lista[index]:
        menor_valor = lista[index]
    # criada uma lista vazia, fazemos a divisão de cada valor dentro de "lista" por 2, caso a divisão de resto 0
    # ele é adicionado dentro de "pares"
    if lista[index] % 2 == 0:
        pares.append(lista[index])
    # ele vai verificar quantas vezes o item na posição 0(o numero 12) se repente dentro de lista
    if lista[index] == lista[0]:
        ocorrencias_item1 = ocorrencias_item1 + 1
    # identifica quais itens dentro de "lista" são negativos e depois os soma
    if lista[index] < 0:
        soma_negativos = soma_negativos + lista[index]
    # usa a variavel "media_elementos" que vai somando cada item dentro de "lista" e no fim divide pelo length
    # de lista para achar a media
    media_elementos = media_elementos + lista[index]
media_elementos = media_elementos / len(lista)
# a) imprima o maior elemento
print(maior_valor)
# b) imprima o menor elemento
print(menor_valor)
# c) imprima os números pares
print(pares)
# d) imprima o número de ocorrência do primeiro elemento da lista
print(ocorrencias_item1)
# e) imprima a média dos elementos
print(media_elementos)
# f) imprima a soma dos elementos de valor negativo
print(soma_negativos)
