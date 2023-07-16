contatos = {
    "rogerio@gmail.com": {"nome": "Rogerio", "idade": 28, "telefone": "2244-1354"},
    "elisa@gmail.com": {"nome": "elisa", "idade": 19, "telefone": "4565-5545", "extras": {"a": 1}},

}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)