contatos = {
    "rogerio@gmail.com": {"nome": "Rogerio", "telefone": "3333-2221"}
}

print(contatos.popitem()) # ('rogerio@gmail.com', {'nome': 'Rogerio', 'telefone': '3333-2221'})

print(contatos.popitem()) # KeyError: 'popitem(): dictionary is empty'