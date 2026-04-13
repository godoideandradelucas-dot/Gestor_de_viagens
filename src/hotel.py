from utils import validar_hotel, validar_local, validar_preco, validar_tipo_hotel, isEqual

hoteis = []

def adicionar_hotel():
    print("\n=== ADICIONAR HOTEL ===")

    nome_hotel =  validar_hotel()
    local = validar_local()
    preco = validar_preco()
    tipo_hotel = validar_tipo_hotel()


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

    print("\n=== LISTA DE HOTÉIS ===")
    for hotel in hoteis:
        for chave, valor in hotel.items():
            print(chave,":",valor)
        print()
    return 200, "Sucesso"


def consultar_hotel():
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== CONSULTAR HOTEL ===")
    nome = input("Nome do hotel para consultar:").strip

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


def atualizar_hotel():
    if not hoteis:
        return 404, "Não existem hoteis registados."

    print("\n=== ATUALIZAR HOTEL ===")
    nome = input("Digite o nome do hotel para atualizar: ").strip()

    if not nome:
        return 400, "Hotel não encontrado."

    for hotel in hoteis:
        if nome.lower() in hotel["nome"].lower():
            print("Digite os novos dados")
            hotel["nome"] = validar_hotel()
            hotel["local"] = validar_local()
            hotel["preco"] = validar_preco()
            hotel["tipo"] = validar_tipo_hotel()
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
