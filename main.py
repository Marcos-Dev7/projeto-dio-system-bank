from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

# . Constantes de controle de cor.

COLOR_VERMELHO = "\033[31m"
COLOR_RESET = "\033[0m"
COLOR_AZUL = "\033[94m"
COLOR_AMARELO = "\033[33m"
COLOR_GREEN = "\033[32m"

clientes = []
contas = []

# 1.1 Criar Classes e Objetos para modelar o aplicativo.
class Conta:
    def __init__(self,saldo, numero, agencia, cliente, historico): #Saldo tipo float, numero tipo int, agencia tipo str, cliente vai receber Cliente, historico.
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    @classmethod
    def nova_conta(cls, cliente, numero): #Metodo pra criar conta que retorne um objeto Conta
        return cls(cliente, numero)
    
    @property
    def saldo(self): #Metodo para visualizar saldo
        return self._saldo
    
    @property
    def numero(self):
        return self._saldo
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico (self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print(f"{COLOR_VERMELHO}Operação Falha! Seu saldo e insuficiente para realizar o saque!{COLOR_RESET}")

        elif valor > 0:
            self.saldo -= valor
            print(f"{COLOR_GREEN} Saque Realizado com sucesso no valor de R$ {valor:.2f}!{COLOR_RESET}")
            return True
        
        else:
            print("\n Operação falhou! o valor é invalido.")
            return False
        
    def depositar (self, valor):
        if valor > 0:
            self._saldo += valor
            print(f" {COLOR_GREEN} Deposito no valor de R$ {valor:.2f} realizado com sucesso!{COLOR_RESET}")
        else:
            print("Operação falhou! O valor informado e invalido")
            return False
        
        return True
class Transacao(ABC): #Classe Abstrata
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self,conta):
        pass
class ContaCorrente(Conta):  #Classe filha com extensão dos atributos limite e limite_saques
    def __init__(self,  numero, cliente, limite=500, limite_saques=3):
        super().__init__(self, numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["Tipo"] == "Saque"]  
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print(f"{COLOR_VERMELHO}Operação Falha! Voçê excedeu o limite de saque por transação!.{COLOR_RESET}")
        
        elif excedeu_saques:
            print(f"{COLOR_VERMELHO}Operação Falha! Você excedeu o limite de saque diário!{COLOR_RESET}")

        else:
            return super().sacar(valor)

        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m_%Y %H:%M:%s"),
            }
        )
class Cliente:
    def __init__(self, endereco,):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        pass

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        pass
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco) 
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
    
    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valorvalor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
# 2. Criei as funçõespass

def menu():
    menu_str = f'''{COLOR_AMARELO}\n    ----- DIO BANK -----{COLOR_RESET}
    {COLOR_AZUL}[1] Depositar
    {COLOR_AZUL}[2] Sacar
    {COLOR_AZUL}[3] Extrato
    {COLOR_AZUL}[4] Cadastrar Usuário
    {COLOR_AZUL}[5] Nova Conta Corrente
    {COLOR_AZUL}[6] Listar Contas
    {COLOR_AZUL}[0] Sair
    {COLOR_AMARELO}--------------------\n{COLOR_RESET}
=>: '''
    return input(menu_str)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return
    
    #FIXME: Não permite cliente escolher a conta
    return cliente.contas[0]

def depositar(clientes):  
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do depósito:"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes): 
    cpf = input("Informe o CPF do cliente")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes): 
    cpf = input("Informe o CPF do cliente:")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n==============  Extrato ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Nçao foram realizadas movimentações. "
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    cpf = input("informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Já existe cliente com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    cliente = PessoaFisica(nome= nome, data_nascimento= data_nascimento, cpf= cpf, endereco= endereco)

    clientes.append(cliente)

    print("Cliente criado com sucesso!")

def criar_conta(numero_conta, clientes, contas): 
    cpf = input("Informe o CPF do cliente")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado, fluxo de criação de conta encerrado!")
        return
    
    conta = ContaCorrente.nova_conta(cliente= cliente, numero= numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n Conta criada com sucesso!")

def listar_contas(contas): 
    for conta in contas:
        print("=" * 100)
        print((str(conta)))

while True: #Loop Menu
    opcao = menu()
        
    if opcao == "1":
        depositar(clientes)

    elif opcao == "2":
        sacar(clientes)

    elif opcao == "3":
        exibir_extrato(clientes)

    elif opcao == "4":
        criar_cliente(clientes)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes, contas)

    elif opcao == "6":
        listar_contas(contas)

    elif opcao == "0":
        print('\n Obrigado por utilizar nossos serviços, volte sempre!\n')
        break
    else:
        print(f"{COLOR_VERMELHO}Operação inválida, por favor selecione novamente a operação desejada.{COLOR_RESET}")