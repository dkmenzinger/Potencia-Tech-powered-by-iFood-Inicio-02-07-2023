#  Listas:
#  Em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
#  Podemos criar listas utilizando o construtor list,
#  a função range ou colocando valores separados por vírgula dentro de conlchetes.
#  Listas são objetos mutáveis, portando podemos alterar seus valores após a criação.

frutas = ["laranja", "maca", "uva", "pera"]
print(frutas)

print(frutas[0]) # laranja
print(frutas[1]) # maca
print(frutas[2]) # uva
print(frutas[3]) # pera

print(frutas[-1]) #  Sequências suportam indexação negativa. A contagem começa em -1.
print(frutas[-2])
frutas = []

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari","F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)
