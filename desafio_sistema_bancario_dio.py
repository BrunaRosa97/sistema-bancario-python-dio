menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair 

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito:  "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f} \n"
        else:
            print("Valor de depósito inválido")    

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Falha! Você não tem saldo suficiente!")

        if excedeu_limite:
            print("Falha! O valor do saque excede o limite!")

        if excedeu_saques:
            print("Falha! Número máximo de saques excedidos!")                

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor: .2f} \n"
            numero_saques += 1

        else:
            print("Desculpe, o valor informado é inválido!")       
    
    elif opcao == "3":
        print(f"*************** EXTRATO *****************\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)        
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"*****************************************\n")

    elif opcao == "0":
        print("Obrigada pela preferêcia, volte sempre!")

        break            

    else:
        print("Selecione uma opção válida")    
          