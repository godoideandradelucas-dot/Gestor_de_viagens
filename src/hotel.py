from utils import isEqual

hoteis = []

def adicionar_hotel(nome_hotel, local, preco, tipo_hotel):
    hotel = {
        "nome": nome_hotel,
        "local": local,
        "preco": preco,
        "tipo": tipo_hotel,
    }
    hoteis.append(hotel)
    return 201, "Hotel adicionado com sucesso."


def ver_hoteis():
    if not hoteis:
        return 404, "Não existem hoteis registados."
    return 200, hoteis


def consultar_hotel(nome):
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== CONSULTAR HOTEL ===")
    if not nome:
        return 400, "Hotel não encontrado."

    encontrado = False
    for hotel in hoteis:
        if nome.lower() in hotel["nome"].lower():
            for chave, valor in hotel.items():
                print(chave, ":", valor)
            print()
            encontrado = True

    if not encontrado:
        return 404, "Hotel não encontrado."
    return 200, "Hotel encontrado."

def atualizar_hotel(nome_procurar, nome_hotel, local, preco, tipo_hotel):
    if not hoteis:
        return 404, "Não existem hoteis registados."

    if not nome_procurar:
        return 400, "Hotel não encontrado."

    for hotel in hoteis:
        if nome_procurar.lower() in hotel["nome"].lower():
            hotel["nome"] = nome_hotel
            hotel["local"] = local
            hotel["preco"] = preco
            hotel["tipo"] = tipo_hotel
            return 200, "Hotel atualizado"

    return 404, "Hotel não encontrado."


def remover_hotel(nome_remover):
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== REMOVER HOTEL ===")
    for hotel in hoteis:
        if isEqual(nome_remover, hotel["nome"]):
            hoteis.remove(hotel)
            return 200, "Hotel removido"
    return 404, "Hotel não encontrado."

#############################################################################################

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
