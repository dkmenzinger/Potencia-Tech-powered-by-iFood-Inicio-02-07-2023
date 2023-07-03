# Na matemática existe uma regra que indica quais operações devem ser executadas primeiro.
# Isso é útil pois ao analisar uma expressão, a depender da ordem das operações o valor pode ser dife	rente:
# A definição indica a seguinte ordem como a correta:
# • Parêntesis
# • Expoêntes
# • Multiplicações e divisões ( da esquerda para a direita)
# • Somas e subtrações ( da esquerda para a direita)


print(10 - 5 * 2)
print((10 -5) * 2)
print(10 ** 2 * 2)
print(10 **(2 * 2))
print(10 / 2 * 4)

produto_1 = 20
produto_2 = 10

print(produto_1 + produto_2 + 3.5)
print(produto_1 - produto_2)
print(produto_1 * produto_2)
print(produto_1 ** produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 % produto_2)

x = (10 + 5) * 4
y = 10 + (5 * 4)
b = (10 / 2) + (36 * 2) - (100 ** 2)
print(x)
print(y)
print(b)