contatos = {
    "rogerio@gmail.com": {"nome": "Rogerio", "idade": 28, "telefone": "2244-1354"},
    "elisa@gmail.com": {"nome": "elisa", "idade": 19, "telefone": "4565-5545", "extras": {"a": 1}},

}

copia = contatos.copy()
copia["rogerio@gmail.com"] = {"nome": "Roger"}

print(copia["rogerio@gmail.com"])

copia["rogerio@gmail.com"]