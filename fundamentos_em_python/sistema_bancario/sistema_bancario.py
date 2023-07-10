menu = """
  Digite uma das Opções

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 1500
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Quanto você gostaria de depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("""
             ========= Valor depositado com sucesso! ========= """)

        else:
            print(""" 
             ========= Desculpe, não foi possível realizar a operação devido a um valor inválido!. ========= 
             ========= Por favor, verifique o valor a ser depositado!. ========= 
               """)

    elif opcao == "1":
        valor = float(input("Qual é o valor que você gostaria de sacar da sua conta?: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("""
             ========= Infelizmente, você não tem saldo suficiente para realizar o saque solicitado.. =========
            """)

        elif excedeu_limite:
            print(""" 
            ========= Desculpe, o valor do saque excede o limite permitido. =========
            ========= Por favor, insira um valor igual ou inferior a R$ 500,00. =========
             """)

        elif excedeu_saques:
            print("""
            ========= Desculpe, você atingiu o número máximo de saques permitidos para hoje.=========
            ========= Por favor, tente novamente amanhã. =========
            """)

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(""""
            ========= Saque efetuado com sucesso! =========
            """)

        else:
            print("""
             ========= Desculpe, não foi possível realizar a operação devido a um valor inválido! =========
             """)

    elif opcao == "2":
        print("\n ========= Extrado ========= ")
        print("Não há histórico de movimentações na conta bancária até o momento." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(" =========================== ")

    elif opcao == "3":
        print(""" ========= Obrigado por ser nosso cliente, volte sempre! =========
                """)
        break


    else:
        print(""" 
             ========= Desculpe, não foi possível realizar a operação!. =========
        """)