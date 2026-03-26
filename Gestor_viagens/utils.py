from datetime import datetime

def verificar_viajantes(viajantes):
    if not viajantes:
        print("Não há viajantes cadastrados!\n")
        return False
    return True

def verificar_destinos(destinos):
    if not destinos:
        print("Não há destinos registrados!\n")
        return False
    return True

def verificar_hoteis(hoteis):
    if not hoteis:
        print("Não há hotéis registrados!\n")
        return False
    return True

### VIAJANTES ###

def validar_nome():
    nome = input("Digite seu nome:")
    while not nome.isalpha():
        nome = input("Digite seu nome(apenas letras):")
    return nome

def validar_data():
    data = input("Digite sua data de nascimento(DD/MM/AAAA):")
    while True:
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: data inválida! Use o formato DD/MM/AAAA")
            data = input("Digite sua data de nascimento(DD/MM/AAAA):")

def validar_nacionalidade():
    nacionalidade = input("Digite sua nacionalidade:")
    while not nacionalidade.replace(" ", "").isalpha():
        nacionalidade = input("Digite sua nacionalidade(apenas letras):")
    return nacionalidade

def validar_telefone():
    telefone = input("Digite seu telefone:")
    while not (telefone.isdigit() and len(telefone) == 9):
        print("Erro: o número deve ter 9 dígitos e só números!")
        telefone = input("Digite novamente: ")
    return telefone

def validar_email():
    email = input("Digite seu email(@gmail.com - @hotmail.com - @outlook.com):")
    while not ("@gmail.com" in email or "@hotmail.com" in email or "@outlook.com" in email):
        print("Erro: email inválido!")
        email = input("Digite seu email novamente (@gmail.com - @hotmail.com - @outlook.com): ")
    return email

def validar_NIF():
    NIF = input("Digite seu NIF:")
    while not (NIF.isdigit() and len(NIF) == 9):
        print("Erro: o NIF deve ter 9 números!")
        NIF = input("Digite seu NIF novamente: ")
    return NIF

def validar_interesses():
    interesses = input("Digite seus interesses(praias, natureza, montanhas):")
    while not interesses.replace(" ", "").isalpha():
        interesses = input("Digite seus interesses(apenas letras):")
    return interesses

def validar_orcamento():
    orcamento = input("Digite seu orçamento(€):")
    while not orcamento.isdigit():
        orcamento = input("Digite seu orçamento(apenas numeros)")
    return orcamento


### DESTINO ###

def validar_pais():
    pais = input("Digite o nome do país:")
    while not pais.replace(" ", "").isalpha():
        pais = input("Digite o nome do país(apenas letras):")
    return pais

def validar_cidade():
    cidade = input("Digite o nome da cidade:")
    while not cidade.replace(" ", "").isalpha():
        cidade = input("Digite o nome da cidade(apenas letras):")
    return cidade

def validar_tipo():
    tipo = input("Digite o tipo de destino (praia, urbano, montanha, natureza):")
    while not tipo.replace(" ", "").isalpha():
        tipo = input("Digite o tipo de destino(apenas letras):")
    return tipo

def validar_atracoes():
    atracoes = input("Digite as atrações principais:")
    while not atracoes.replace(" ", "").isalpha():
        atracoes = input("Digite as atrações principais(apenas letras):")
    return atracoes

### HOTEL ###

def validar_hotel():
    nome_hotel = input("Digite o nome do hotel:")
    while not nome_hotel.replace(" ", "").isalpha():
        nome_hotel = input("Digite o nome do hotel(apenas letras):")
    return nome_hotel

def validar_local():
    local = input("Digite a localizacao(cidade):")
    while not local.replace(" ", "").isalpha():
        local = input("Digite o localizacao(apenas letras):")
    return local

def validar_preco():
    preco = input("Digite o preço por noite(€):")
    while not preco.isdigit():
        preco = input("Digite o preço por noite(apenas numeros):")
    return preco

def validar_tipo_hotel():
    tipo_hotel = input("Digite o tipo de hospedagem (hotel, pousada, resort):")
    while not tipo_hotel.isalpha():
        tipo_hotel = input("Digite o tipo de hospedagem (hotel, pousada, resort):")
    return tipo_hotel
