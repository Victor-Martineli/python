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
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self.historico = Historico()

# quando um elemento esta com um _ antes de seu nome indica que ele não deveria ser alterado de forma direta, porem como
# no python não temos uma classe private isso ainda é possivel porem poderia ser desastroso, então seguimos a convenção
# de não usa-los diretamente, então para modifica-los, usamos os getters e setters para atribuir e mudar seus valores.

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        if saldo < 0:
            print('Saldo não pode ser negativo')
        else:
            self._saldo = saldo

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def deposita(self, valor):
        self._saldo += valor
        self.historico.transacoes.append('depósito de {}'.format(valor))

    def saca(self, valor):
        if self._saldo < 0:
            print('saldo insuficiente')
        elif self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append('saque de {}'.format(valor))
            return True

    def extrato(self):
        print('numero: {} \nsaldo: {}'.format(self._numero, self._saldo))
        self.historico.transacoes.append('tirou extrato - saldo de {}'.format(self._saldo))

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
