class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 1.2


class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

    def autentica(self, senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

class ControleBonificacoes:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        if hasattr(obj, 'get_bonificacao'):
            self._total_bonificacoes += obj.get_bonificacao()
        else:
            print('instância de {} não implementa o metodo get_bonificacao()'.format(self.__class__.__name__))
