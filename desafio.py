from datetime import datetime

menu = f"""
\033[1;36m {35 * "="} \033[1;m
\033[1;36m {'Operações Bancárias':^35} \033[1;m
\033[1;36m {35 * "="} \033[1;m
\033[1;32m[d] Depositar \033[1;m
\033[1;33m[s] Sacar \033[1;m
\033[1;34m[e] Extrato \033[1;m
\033[1;31m[q] Sair \033[1;m
\033[1;36m {35 * "="} \033[1;m
\033[1;36mEscolha uma opção: \033[1;m"""

saldo = 0
limite = 500
extrato = f"\n{35 * '='}\n\033[1;36mExtrato Bancário\033[1;m\n{35 * '='}\n"
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu).strip().lower()
    
    if opcao == "d":
        valor = float(input("\033[1;36mDigite o valor do depósito: \033[1;m")) 
        valor = valor if valor > 0 else valor*-1
        saldo += valor
        extrato += f"\033[1;32mData: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} Operação: DEPOSITO; Valor: {valor:.2f}\033[1;m\n"
        
        print(f"\n{35 * '-'}")
        print(f"\033[1;32mDepósito efetuado com sucesso! Valor depositado: R$ {valor:.2f}\033[1;m")
        print(f"{35 * '-'}")
        
    elif opcao == "s":
        if numero_saques != LIMITE_SAQUES:
            valor = float(input("\033[1;33mDigite o valor do saque: \033[1;m"))
            
            if valor > limite:
                print("\033[1;31mValor maior que o limite permitido!\033[1;m")
                
            else:    
                valor = valor if valor > 0 else valor*-1
                saldo -= valor
                numero_saques += 1
                extrato += f"\033[1;31mData: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} Operação: SAQUE; Valor: {valor:.2f}\033[1;m\n"
                
                print(f"\n{35 * '-'}")
                print(f"\033[1;33mSaque efetuado com sucesso! Valor sacado: R$ {valor:.2f}\033[1;m")
                print(f"{35 * '-'}")    
                
        else:
            print(f"\n{35 * '='}")
            print("\033[1;31mLimite de Saque Excedido!\033[1;m")
            print(f"{35 * '='}")
        
    elif opcao == "e":
        print(extrato)
        print(f"{35 * '-'}")
        print(f"\033[1;34mSaldo atual: R$ {saldo:.2f}\033[1;m")
        print(f"{35 * '-'}")
        
    elif opcao == "q":
        print(f"\n{35 * '='}")
        print("\033[1;35mObrigado, volte sempre!\033[1;m")
        print(f"{35 * '='}")
        break
    
    else:
        print(f"\n{35 * '='}")
        print("\033[1;31mOpção inválida, por favor selecione novamente a operação desejada.\033[1;m")
        print(f"{35 * '='}")