from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

import textwrap

def menu(): 
    menu = """

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tNova Conta
    [6]\tListar conta
    [0]\tSair
     
    => """

    return input(textwrap.dedent(menu))

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.agencia = "0001"
        self.historico = Historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self.saldo
    @property
    def numero(self):
        return self.numero
    @property
    def agencia(self):
        return self.agencia
    @property
    def cliente(self):
        return self.cliente
    @property
    def historico(self):
        return self.historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falou! O valor informado é inválido. @@@")

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("=== Valor depositado com sucesso! ===")
            
        else:
            print("\n@@@ Operação falhou! O valor do depósito é inválido" )
            return False

        return True
     
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacao if transacao["tipo"] == Saque.__name__])

class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self.transacoes
    
    def adicionar_transacao(self, transacao):
        self.transacao.append(
        {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime('%d-%m-%Y %H:%M:%s'),

        }
    )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adiconar_transacao(self.valor)

def main():
    clientes = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)
           
        elif opcao == "2":
            sacar(clientes)

           
        elif opcao == "3":
           exibir_extrato(clientes)

        elif opcao == "4":
            criar_clientes(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
             listar_contas(contas)

        elif opcao == "q":
             break
        
        else:
            print("\n@@@ Operção inválida! Por favor selecione novamente a opção desejada. @@@")

main()