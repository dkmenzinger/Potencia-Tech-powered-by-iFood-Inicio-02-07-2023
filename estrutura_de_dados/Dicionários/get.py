contatos = {
    "rogerio@gmail.com": {"nome": "Rogerio", "telefone": "3333-2221"}
}

# contatos["chave"] #KeyError: 'chave'

print(contatos.get("chave")) # None
print(contatos.get("chave", {})) # {}
print(contatos.get("rogerio@gmail.com", {})) # {'nome': 'Rogerio', 'telefone': '3333-2221'}