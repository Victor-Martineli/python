# conjuntos são indicados por {}
frutas = {'maça', 'uva', 'laranja', 'pera'}

# é possivel fazer operações matemáticas com os objetos de um conjunto
a = set('abacate')
b = set('abacaxi')
print(a - b)
# diferença
print(a | b)
# união
print(a & b)
# interseção
print(a ^ b)
# diferença simétrica
# obs: para criar um conjunto vazio vc usa set() e não {}


