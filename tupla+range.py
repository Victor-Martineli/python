dias = ('domingo', 'segundo', 'terceiça', 'quarta', 'quinta', 'sexta', 'sabado')

# a tupla vai se assemelhar muito a uma variavel pois os () são opcionais
# porem é recomendavel coloca-los para evitar se confundir na hora de trabalhar

lista = [3, 4]
tupla = (1, 2, lista)

# não é possivel atribuir itens individuais em uma tupla, mas
# podemos colocar dentro dela uma lista de objetos mutaveis dentro dela
print(tupla)
lista = [4, 4]
tupla = (1, 2, lista)
print(tupla)
# quando é necessário armazenar uma coleção de dados que não possa ser alterada prefira usar tuplas

# range()
# range precisa ser usado em um loop, ele é uma sequencia imutavel de numeros tendo seu inicio e fim

for valor in range(1, 3):
    print(valor)

# também é possivel controlar a variação da sequencia dentro de range
# no caso ele vai de 1 a 10, de 2 em 2 numeros
for valor in range(1, 10, 2):
    print(valor)
