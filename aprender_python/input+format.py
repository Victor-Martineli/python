#input
nome = input("digite seu nome: \n")
#print("seu nome é " + nome)

#format, é usado junto ao {}
idade = input("digite sua idade: \n")
print("seu nome é {} e sua idade é {}".format(nome, idade))

#format também pode ser usada para arredondar um float
x = 245.34525
print('{:.2f}'.format(x))

#IMPORTANTE: O	operador ==	é usado	para verificar	se	algo 
#é	igual	a	outro.	Não	confundir	com	o	=	,	que	atribui um
#	valor	a	uma	variável.
#Também	podemos	verificar	se	um	número	é	maior,	utilizando
#	o	operador(	>	), ou	menor	(	<	)	do	que	outro:


#Podemos também	utilizar a função bool() para fazer a verificação:
print (bool(3 > 5))
