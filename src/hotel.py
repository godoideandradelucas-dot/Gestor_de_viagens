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
    return 201, "Sucesso"


def ver_hoteis():
    if not hoteis:
        return 404, "Não existem hoteis registados."

    return 200, hoteis


def consultar_hotel():
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== CONSULTAR HOTEL ===")
    nome = input("Nome do hotel para consultar:").strip()
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
    return 200, "Sucesso"


def atualizar_hotel(nome_hotel, local, preco, tipo_hotel):
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== ATUALIZAR HOTEL ===")
    nome = input("Digite o nome do hotel para atualizar: ").strip()

    if not nome:
        return 400, "Hotel não encontrado."

    for hotel in hoteis:
        if nome.lower() in hotel["nome"].lower():
            hotel["nome"] = nome_hotel
            hotel["local"] = local
            hotel["preco"] = preco
            hotel["tipo"] = tipo_hotel
            return 200, "Sucesso"

    return 404, "Hotel não encontrado."


def remover_hotel():
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== REMOVER HOTEL ===")
    nome_remover = input("Digite o nome do hotel para remover:")

    for hotel in hoteis:
        if isEqual(nome_remover, hotel["nome"]):
            hoteis.remove(hotel)
            return 200, "Sucesso"

    return 404, "Hotel não encontrado."
