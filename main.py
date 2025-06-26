COLOR_VERMELHO = "\033[31m"
COLOR_RESET = "\033[0m"
COLOR_AZUL = "\033[94m"
COLOR_AMARELO = "\033[33m"
COLOR_GREEN = "\033[32m"

menu = f'''{COLOR_AMARELO}\n ----- DIO BANK -----{COLOR_RESET}
 {COLOR_AZUL}[1] Depositar
 {COLOR_AZUL}[2] Sacar
 {COLOR_AZUL}[3] Extrato
 {COLOR_AZUL}[0] Sair
 {COLOR_AMARELO}--------------------\n{COLOR_RESET}
 =>: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)
        
    if opcao == "1":
        valor = float(input(" Digite o valor R$: "))

        if valor > 0: 
            saldo += valor
            extrato += f"{COLOR_GREEN} Deposito de R${valor:.2f} realizado com sucesso!\n{COLOR_RESET}"
            print(f" {COLOR_GREEN} Deposito no valor de R$ {valor:.2f} realizado com sucesso!{COLOR_RESET}")

        else:
            print(f"{COLOR_VERMELHO}Operação Invalida! Não é possivel depositar valores negativos.{COLOR_RESET}") 

    elif opcao == "2":
            saque = float(input('Digite o valor desejado para saque: '))
            
            if saque <= saldo:
                 if saque <= limite:
                      if numero_saques < LIMITE_SAQUE:
                           saldo -= saque
                           numero_saques += 1
                           extrato += f"{COLOR_GREEN} Saque no valor de R${saque:.2f} realizado com sucesso!{COLOR_RESET}\n"
                           print(f"{COLOR_GREEN} Saque Realizado com sucesso no valor de R$ {saque:.2f}!{COLOR_RESET}")
                      else:
                           print(f"{COLOR_VERMELHO}Operação Falha! Voçê excedeu o limite de saque diario!{COLOR_RESET}")
                 else:
                      print(f"{COLOR_VERMELHO}Operação Falha! Voçê excedeu o limite de saque por transação!.{COLOR_RESET}")
            else:
                 print(f"{COLOR_VERMELHO}Operação Falha! Seu saldo e insuficiente para realizar o saque!{COLOR_RESET}")

    elif opcao == "3":
        header = " EXTRATO "
        print(header.center(50, '='))
        
        if not extrato:
             print(" Não foram realizadas movimentações!")
        else:
            print(f"\n{extrato}")
     
        print(f"==================================================")
        print(f" Saldo atual: {COLOR_GREEN} R$ {saldo:.2f}{COLOR_RESET}")

    elif opcao == "0":
         print('\n Obrigado por utilizar nossos serviços, volte sempre!\n')
         break
    
    else:
         print(f'{COLOR_VERMELHO}Opção Invalida! Tente novamente.\n{COLOR_RESET}')       
        
        
        
        


           



