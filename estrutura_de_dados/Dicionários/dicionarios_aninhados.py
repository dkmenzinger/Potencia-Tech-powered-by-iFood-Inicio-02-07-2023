contatos = {
    "rogerio@gmail.com": {"nome": "Rogerio", "idade": 28, "telefone": "2244-1354"},
    "elisa@gmail.com": {"nome": "elisa", "idade": 19, "telefone": "4565-5545", "extras": {"a": 1}},

}

print(contatos["rogerio@gmail.com"]["idade"]) # para acessar

extras = contatos["elisa@gmail.com"]["extras"]["a"]
print(extras)