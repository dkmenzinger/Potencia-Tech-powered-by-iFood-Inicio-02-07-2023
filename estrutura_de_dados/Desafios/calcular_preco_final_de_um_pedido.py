valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

def calcular_pedido(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago):

    valorTotalHamburgueres = valorHamburguer * quantidadeHamburguer

    valorTotalBebida = valorBebida * quantidadeBebida

    precoTotalPedido = valorTotalHamburgueres + valorTotalBebida

    troco = valorPago - precoTotalPedido

    saida = f"O preço final do pedido é R$ {precoTotalPedido:.2f}. Seu troco é R$ {troco:.2f}."

    return saida

resultado = calcular_pedido(valorHamburguer, quantidadeHamburguer, valorBebida, quantidadeBebida, valorPago)
print(resultado)