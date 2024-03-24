
# listas podem ser compostas de int, float e string
lista = [1,2,3,4]
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