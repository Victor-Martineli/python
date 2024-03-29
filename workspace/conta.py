import datetime
# criando uma classe em python


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print('data de abertura: {}'.format(self.data_abertura))
        print('transações: ')
        for t in self.transacoes:
            print('-', t)


class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf


class Conta:

    # com o metodo __init__ podemos criar uma classe que nos obriga a passar todos os valores dentro do (),
    # caso contrario ele responderá um erro
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        # podemos deixa tanto atributos sem valor, para que eles sejam especificados caso a caso ou podemos passar
        # um valor padrão que pode ser alterado caso seja necessário, como o limite da conta
        print('Iniciazando uma conta')
        # self é a referência do objeto
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append('depósito de {}'.format(valor))

    def saca(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append('saque de {}'.format(valor))
            return True

    def extrato(self):
        print('numero: {} \nsaldo: {}'.format(self.numero, self.saldo))
        self.historico.transacoes.append('tirou extrato - saldo de {}'.format(self.saldo))

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if not retirou:
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append('transferência de {} para conta {}'.format(valor, destino.numero))
            return True

# quando criamos um novo objeto não precisamos do metodo __new__ pois o proprio python o está executando por baixo dos
# panos, logo em seguida usa o metodo __init__ ptoda vez que criamos uma conta nova


cliente1 = Cliente('Victor', 'Pierobon', '1234')
c1 = Conta('123-4', cliente1, 500.0)
cliente2 = Cliente('Gabriel', 'Viamonte', '2345')
c2 = Conta('123-5', cliente2, 200.0)

c1.deposita(100)
c1.saca(75)
c1.transfere_para(c2, 200)
c1.extrato()
c1.historico.imprime()
