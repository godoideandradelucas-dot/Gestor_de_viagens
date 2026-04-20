from datetime import datetime

def isEqual(nome_1, nome_2):
    return nome_1.lower() == nome_2.lower()

def validar_data(data_nascimento):
    while True:
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
            return data_nascimento
        except ValueError:
            print("Erro: data inválida! Use o formato DD/MM/AAAA")
            data_nascimento = input("Digite sua data de nascimento(DD/MM/AAAA):")


def validar_telefone(telefone):
    while not (telefone.isdigit() and len(telefone) == 9):
        print("Erro: o número deve ter 9 dígitos e só números!")
        telefone = input("Digite novamente: ")
    return telefone


def validar_email(email):
    while not ("@gmail.com" in email or "@hotmail.com" in email or "@outlook.com" in email):
        print("Erro: email inválido!")
        email = input("Digite seu email novamente (@gmail.com - @hotmail.com - @outlook.com): ")
    return email


def validar_NIF(NIF):
    while not (NIF.isdigit() and len(NIF) == 9):
        print("Erro: o NIF deve ter 9 números!")
        NIF = input("Digite seu NIF novamente: ")
    return NIF
