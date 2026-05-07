hoteis = []
_proximo_id_hotel = 1


def adicionar_hotel(nome_hotel, local, preco, tipo_hotel):
    global _proximo_id_hotel
    hotel = {
        "id": _proximo_id_hotel,
        "nome": nome_hotel,
        "local": local,
        "preco": preco,
        "tipo": tipo_hotel,
    }
    _proximo_id_hotel += 1
    hoteis.append(hotel)
    return 201, hotel


def ver_hoteis():
    if not hoteis:
        return 404, "Não existem hoteis registados."
    return 200, hoteis


def consultar_hotel(id):
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== CONSULTAR HOTEL ===")
    for hotel in hoteis:
        if hotel["id"] == id:
            return 200, hotel

    return 404, "Hotel não encontrado."


def atualizar_hotel(id, nome_hotel, local, preco, tipo_hotel):
    if not hoteis:
        return 404, "Não existem hoteis registados."

    for hotel in hoteis:
        if hotel["id"] == id:
            hotel["nome"] = nome_hotel
            hotel["local"] = local
            hotel["preco"] = preco
            hotel["tipo"] = tipo_hotel
            return 200, hoteis

    return 404, hoteis


def remover_hotel(id):
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== REMOVER HOTEL ===")
    for hotel in hoteis:
        if hotel["id"] == id:
            hoteis.remove(hotel)
            return 200, hoteis

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
