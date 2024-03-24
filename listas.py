
# listas podem ser compostas de int, float e string
lista = [1, 2, 3, 4]
# se quisemos que apenas um elemento específico de uma lista seja exibido
# basta utilizar o seguinte comando
print(lista[2])

meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
n = 1

while(n < 4):
    mes = int(input('escolha um mês(1-12): '))
    if 1 <= mes < 13:
        print('o mês é {} '.format(meses[mes-1]))
    n += 1

lista2 = [2, 3, 5, 7, 11]
# outras operações que podem ser feitas com listas são as seguintes

print(lista2[0:2])
# ou print(lista2[:2]) que vamos pegar até o item 2 da lista

print(lista2[2:])
# vai pegar do item 2 em diante até o fim da lista

print(lista2[-3:])
# colocando o - invertemos a ordem, pega do final para o começo

print(lista2[2:4])
# pega um recorte da lista

lista3 = []

lista3.append('zero')
print(lista3)
# a função append() adiciona um elemento por vez na lista
# para inserir mais elementos pode-se somar ou multiplicar listas
# outra opção também é usar a função extend()
lista3.extend(['dois', 'tres'])
print(lista3)

lista3 += ['um']
print(lista3)

lista3 *= 2
print(lista3)

# com esse loop podemos exibir cada valor separadamente
for valor in lista3:
    print(valor)