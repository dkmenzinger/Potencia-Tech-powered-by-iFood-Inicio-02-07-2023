# Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

def salvar_carro(marca, modelo, ano, placa):
    # salvar carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-3252")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-3252")


