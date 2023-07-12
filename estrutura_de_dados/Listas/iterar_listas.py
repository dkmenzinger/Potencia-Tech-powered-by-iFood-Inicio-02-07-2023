numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

par = [numero for numero in numeros if numero % 2 == 0]

print(par)

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares) # selecionou os números pares da lista!

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

print(quadrado)

quadrado = [numero ** 2 for numero in numeros]

print(quadrado)
