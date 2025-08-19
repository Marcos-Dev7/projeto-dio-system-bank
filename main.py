from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime

# . Constantes de controle de cor.

COLOR_VERMELHO = "\033[31m"
COLOR_RESET = "\033[0m"
COLOR_AZUL = "\033[94m"
COLOR_AMARELO = "\033[33m"
COLOR_GREEN = "\033[32m"

# 1. Variaveis Globais

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
usuarios = []
AGENCIA = "0001"
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
    
    @abstractclassmethod
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
    
    def adicionar_transacao(transacao):
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
        sucesso_transacao = conta.depositar(self,valor)

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

def depositar(saldo, valor, extrato):  #Receber apenas por posição
    if valor > 0: 
            saldo += valor
            extrato += f"{COLOR_GREEN} Deposito de R${valor:.2f} realizado com sucesso!\n{COLOR_RESET}"
            print(f" {COLOR_GREEN} Deposito no valor de R$ {valor:.2f} realizado com sucesso!{COLOR_RESET}")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques,limite_saques): 
    if valor <= saldo:
        if valor <= limite:
            if numero_saques < LIMITE_SAQUE:
                saldo -= valor
                numero_saques += 1
                extrato += f"{COLOR_GREEN} Saque no valor de R${valor:.2f} realizado com sucesso!{COLOR_RESET}\n"
                print(f"{COLOR_GREEN} Saque Realizado com sucesso no valor de R$ {valor:.2f}!{COLOR_RESET}")
                if numero_saques >= limite_saques:
                    print(f"{COLOR_VERMELHO}Operação Falha! Você excedeu o limite de saque diário!{COLOR_RESET}")
            else:
                print(f"{COLOR_VERMELHO}Operação Falha! Voçê excedeu o limite de saque diario!{COLOR_RESET}")
        else:
            print(f"{COLOR_VERMELHO}Operação Falha! Voçê excedeu o limite de saque por transação!.{COLOR_RESET}")
    else:
        print(f"{COLOR_VERMELHO}Operação Falha! Seu saldo e insuficiente para realizar o saque!{COLOR_RESET}")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/,*, extrato): #hibrido (posicional e nomeado)
    header = " EXTRATO "
    print(header.center(50, '='))
        
    if not extrato:
            print(" Não foram realizadas movimentações!")
    else:
            print(f"\n{extrato}")
    
    print(f"==================================================")
    print(f" Saldo atual: {COLOR_GREEN} R$ {saldo:.2f}{COLOR_RESET}")

def criar_usuario(nome, data_nascimento, cpf, endereco, lista_usuarios):
    cpf_str = str(cpf)

    #Validação
    if not cpf_str.isdigit():
        print("Erro: O CPF deve conter apenas numeros.")
        return None
    
    cpf = int(cpf_str)

    for usuario_existente in lista_usuarios:
        if usuario_existente['cpf'] == cpf:
            print('Erro, Já existe um usuario com este cpf')
            return None
        
    #Se Passar pela validação.     
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "cpf": cpf
    }
    lista_usuarios.append(novo_usuario)
    print('Usuario criado com sucesso!')
    return novo_usuario

def criar_conta_corrente(agencia, cpf_usuario, lista_usuarios, lista_contas): 
    usuario_encontrado = None
    for usuario in lista_usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print(f"{COLOR_VERMELHO}Erro: Usuário com CPF {cpf_usuario} não encontrado. Não é possível criar a conta.{COLOR_RESET}")
        return None

    novo_numero_conta = len(lista_contas) + 1

    nova_conta = {
        "agencia": agencia,
        "numero_conta": novo_numero_conta,
        "cpf_titular": usuario_encontrado['cpf'],

    }
    lista_contas.append(nova_conta) 
    print(f"{COLOR_GREEN}Conta corrente {nova_conta['numero_conta']} (Agência: {agencia}) criada para {usuario_encontrado['nome']} (CPF: {usuario_encontrado['cpf']}).{COLOR_RESET}")
    return nova_conta

def listar_contas(lista_contas): 
    if not lista_contas:
        print(f"{COLOR_AMARELO}Não há contas cadastradas.{COLOR_RESET}")
        return

    print(f"{COLOR_AMARELO}\n--- CONTAS CADASTRADAS ---{COLOR_RESET}")
    for conta in lista_contas:
        nome_titular = "Desconhecido"
        for user in usuarios:
            if user['cpf'] == conta['cpf_titular']:
                nome_titular = user['nome']
                break
        
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {nome_titular} (CPF: {conta['cpf_titular']})")
    print(f"{COLOR_AMARELO}--------------------------{COLOR_RESET}")

while True: #Loop Menu
    opcao = menu()
    
    if opcao == "1":
        valor = float(input(" Digite o valor R$: "))
        saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "2":
        saque = float(input('Digite o valor desejado para saque: '))

        saldo, extrato, numero_saques = sacar(
            saldo= saldo,
            valor= saque,
            extrato= extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques= LIMITE_SAQUE
        )
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == "4":
        nome = input('Digite o seu nome:').lower()
        data_nascimento = input('Data de nascimento (DD-MM-AAAA): ')
        endereco = input('Logradouro, numero, bairro, cidade/uf: ').lower()
        cpf_input= (input('Digite seu CPF (apenas números): '))
        usuario_criado = criar_usuario(
             nome=nome,
             data_nascimento= data_nascimento,
             endereco=endereco,
             cpf= cpf_input,
             lista_usuarios= usuarios
        )
    elif opcao == "5":
        cpf_conta = int(input("Digite o CPF do Usuario Para Criar a Conta: "))
        criar_conta_corrente(
            agencia= AGENCIA,
            cpf_usuario= cpf_conta,
            lista_usuarios= usuarios,
            lista_contas= contas
        )
    elif opcao == "6":
        listar_contas(contas)
    elif opcao == "0":
        print('\n Obrigado por utilizar nossos serviços, volte sempre!\n')
        break
    else:
        print(f"{COLOR_VERMELHO}Operação inválida, por favor selecione novamente a operação desejada.{COLOR_RESET}")