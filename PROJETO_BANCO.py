saldo = 0.0
extrato = ""
NUM_SAQUES = 0

menu = """-------------
      Operações:
        1 - Depósito
        2 - Saque
        3 - Extrato
        0 - Sair 
-------------"""


while True: 

    print(menu)
    opcao = int(input("Digite a operação desejada: "))
    
    if opcao == 1: #Deposito
      valor = float(input("Digite o valor a ser depositado: "))

      if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
      else:
        print("Valor informado e invalido.")


    elif opcao == 2: #Saque
      valor = float(input("Digite o valor do saque: "))
      
      if valor > 500:
        print("Valor excede limite de R$500.")
      
      elif NUM_SAQUES >= 3:
        print("Limite de saques diários já foi atingido.")
        
      elif valor > saldo:
        print("Saldo insuficiente.")  
      
      else:
        NUM_SAQUES += 1 
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        
      
      
    elif opcao == 3: #Extrato
      print("\n------ EXTRATO ------")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("---------------------")
      
    elif opcao == 0: #Sair
      print("Obrigado por usar nosso sistema!")
      break
      
      
    else:
      print("Operação inválida, por favor digite novamente a operação desejada")
