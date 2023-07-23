valorPedido = float(input())

def verificar_brinde_especial(valorPedido):
    if valorPedido >= 50:
        mensagem = "Parabens, você ganhou uma sobremesa gratis!"
    else:
        mensagem = "Que pena, você nao ganhou nenhum brinde especial."

    return mensagem


resultado = verificar_brinde_especial(valorPedido)

print(resultado)
