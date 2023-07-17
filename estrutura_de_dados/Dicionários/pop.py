contatos = {
    "rogerio@gmail.com": {"nome": "Rogerio", "telefone": "3333-2221"}
}

print(contatos.pop("rogerio@gmail.com")) # {'nome': 'Rogerio', 'telefone': '3333-2221'}.

print(contatos.pop("rogerio@gmail.com", {})) # {}