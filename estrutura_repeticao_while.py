opcao = -1


while opcao != 0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo o extrado ...")

else:
    print("Obrigado por usar nosso sistema bancário, até logo!")