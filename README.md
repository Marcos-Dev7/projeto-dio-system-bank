# 🏦 Projeto Sistema Bancário - DIO (v1)
Este repositório contém a segunda versão (v2) de um sistema bancário simples, desenvolvido como parte de um desafio prático da Digital Innovation One (DIO). Esta versão expande as funcionalidades da v1, introduzindo a modularização do código e novas operações para gerenciamento de usuários e contas.

## ✨ Funcionalidades (v1)
Nesta versão aprimorada, as seguintes funcionalidades foram implementadas:

Modularização: O código foi refatorado e dividido em funções menores para melhorar a organização, legibilidade e manutenção.

Depósito: Permite ao usuário depositar um valor em sua conta.

Saque: Permite ao usuário sacar um valor de sua conta, com validações (ex: limite de saque, saldo suficiente).

Extrato: Exibe o histórico de todas as transações (depósitos e saques) realizadas na conta.

Cadastro de Usuários: Nova funcionalidade que permite cadastrar usuários, armazenando informações como nome, data de nascimento, CPF e endereço. Inclui validação para garantir que o CPF seja único e contenha apenas números.

Criação de Contas Correntes: Nova funcionalidade que permite criar contas correntes associadas a um usuário existente. Cada conta tem um número único e é vinculada a um CPF cadastrado.

Listagem de Contas: Permite visualizar todas as contas correntes cadastradas no sistema, mostrando agência, número da conta e titular.

## 🛠️ Tecnologias Utilizadas
Linguagem: Python

Ferramentas: Git para controle de versão

## 🚀 Como Rodar o Projeto
Siga os passos abaixo para configurar e executar o projeto em sua máquina local:

1. **Clone o repositório:**
```
git clone https://github.com/SEU_USUARIO/projeto-dio-system-bank.git
```
2. **Navegue até o diretório do projeto:**
```
cd projeto-dio-system-bank
```
3. **Execute o programa:**
```
python main.py
```
## 📄 Licença
Este projeto está licenciado sob a licença [MIT License](https://opensource.org/licenses/MIT). Veja o arquivo LICENSE para mais detalhes.

## 🧑‍💻 Autor
* **[Marcos-Dev7](https://github.com/Marcos-Dev7)**
