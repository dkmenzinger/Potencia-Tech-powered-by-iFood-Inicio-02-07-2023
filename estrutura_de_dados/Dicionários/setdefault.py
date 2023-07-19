contato = {"nome": "Rogerio", "telefone": "2225-1125"}

# Se ja existe no dicionário ele não ira incluir no mesmo.
contato.setdefault("nome", "Elisa") # {'nome': 'Rogerio', 'telefone': '2225-1125'}
print(contato)

# Se não existe no dicionário ele ira incluir
contato.setdefault("idade", 28) # {'nome': 'Rogerio', 'telefone': '2225-1125', 'idade': 28}
print(contato)