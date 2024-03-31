class Conta:
    _total_contas = 0

    def __init__(self, saldo=0.0):
        self._saldo = saldo
        Conta._total_contas += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print('saldo não pode ser negativo')
        else:
            self._saldo = saldo
# funciona tanto com @staticmethod ou @classmethod então qual devemos usar?
# @classmethod servem para defeinir um método que opera na classe e não em intancias,
# já @staticmethod são usados quando não precisamos receber a referência de um objeto especial e funciona
# como uma função comum, sem relação
    @classmethod
    def get_total_contas(cls):
        return Conta._total_contas


