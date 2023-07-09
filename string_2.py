nome = "Rogerio"
idade = 33
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28,"saldo": 45.435}

print("nome: %s idade: %d" % (nome,idade))    # Essa forma com % não é mais tão utilizado

print("nome: {} idade: {}".format(nome,idade))# Essa forma com format não é mais tão utilizado
print("nome: {1} idade: {0}".format(idade,nome))

print("nome: {1} idade: {0} nome: {1} {1}".format(idade, nome))
print("nome: {nome} idade: {idade}".format(nome=nome, idade=idade ))
print(f"nome: {nome} idade: {idade}".format(**dados))

print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.2f}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:.1f}")