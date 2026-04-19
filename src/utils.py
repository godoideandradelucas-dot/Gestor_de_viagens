from datetime import datetime

def isEqual(nome_1, nome_2):
    return nome_1.lower() == nome_2.lower()

### VIAJANTES ###

def validar_nome(nome):
    while not nome.replace(" ", "").isalpha():
        nome = input("Digite seu nome(apenas letras):")
    return nome


def validar_data(data_nascimento):
    while True:
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
            return data_nascimento
        except ValueError:
            print("Erro: data inválida! Use o formato DD/MM/AAAA")
            data_nascimento = input("Digite sua data de nascimento(DD/MM/AAAA):")


def validar_nacionalidade(nacionalidade):
    while not nacionalidade.replace(" ", "").isalpha():
        nacionalidade = input("Digite sua nacionalidade(apenas letras):")
    return nacionalidade


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


def validar_interesses(interesses):
    while not interesses.replace(" ", "").replace(",", "").isalpha():
        interesses = input("Digite seus interesses(ex: praias, natureza, montanhas):")
    return interesses


def validar_orcamento(orcamento):
    while not orcamento.isdigit():
        orcamento = input("Digite seu orçamento(apenas numeros):")
    return orcamento


### DESTINO ###

def validar_pais(pais):
    while not pais.replace(" ", "").isalpha():
        pais = input("Digite o nome do país(apenas letras):")
    return pais


def validar_cidade(cidade):
    while not cidade.replace(" ", "").isalpha():
        cidade = input("Digite o nome da cidade(apenas letras):")
    return cidade


def validar_tipo(tipo):
    while not tipo.replace(" ", "").isalpha():
        tipo = input("Digite o tipo de destino(apenas letras):")
    return tipo


def validar_atracoes(atracoes):
    while not atracoes.replace(" ", "").replace(",", "").isalpha():
        atracoes = input("Digite as atrações principais(apenas letras e vírgulas):")
    return atracoes

### HOTEL ###

def validar_hotel(nome_hotel):
    while not nome_hotel.replace(" ", "").isalpha():
        nome_hotel = input("Digite o nome do hotel(apenas letras):")
    return nome_hotel


def validar_local(local):
    while not local.replace(" ", "").isalpha():
        local = input("Digite a localizacao(apenas letras):")
    return local


def validar_preco(preco):
    while not preco.isdigit():
        preco = input("Digite o preço por noite(apenas numeros):")
    return preco


def validar_tipo_hotel(tipo_hotel):
    while not tipo_hotel.isalpha():
        tipo_hotel = input("Digite o tipo de hospedagem (hotel, pousada, resort):")
    return tipo_hotel
