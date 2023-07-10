nome = "roGErIo"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá Mundo!   "

print(texto)
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))

for letra in menu:             # exemplo sem a string join
    print(letra, end="-")
print()

print("-".join(menu))  # com a string join fica tudo mais simples.