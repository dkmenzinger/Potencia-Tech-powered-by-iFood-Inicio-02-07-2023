contatos = {
    "rogerio@gmail.com": {"nome": "Rogerio", "telefone": "3333-2221"}
}

contatos.update({"rogerio@gmail.com": {"nome": "Roger"}}) # {'rogerio@gmail.com': {'nome': 'Roger'}}
print(contatos)

contatos.update({"rogerio@gmail.com":{"nome": "Elisa", "telefone": "2455-8956"}})
print(contatos)

# {'rogerio@gmail.com': {'nome': 'Elisa', 'telefone': '2455-8956'}}