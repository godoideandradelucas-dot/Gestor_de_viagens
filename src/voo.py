voos = []
_proximo_id_voo = 1


def adicionar_voo(companhia, origem, id_destino, data_partida, data_chegada, preco):
    global _proximo_id_voo
    voo = {
        "id": _proximo_id_voo,
        "companhia": companhia,
        "origem": origem,
        "id_destino": id_destino,
        "data_partida": data_partida,
        "data_chegada": data_chegada,
        "preco": preco,
    }
    _proximo_id_voo += 1
    voos.append(voo)
    return 201, voo


def ver_voos():
    if not voos:
        return 404, "Não existem voos registados."
    return 200, voos


def consultar_voo(id):
    if not voos:
        return 404, "Não existem voos registados."

    print("\n=== CONSULTAR VOO ===")
    for voo in voos:
        if voo["id"] == id:
            return 200, voo

    return 404, "Voo não encontrado."


def atualizar_voo(id, companhia, origem, id_destino, data_partida, data_chegada, preco):
    if not voos:
        return 404, "Não existem voos registados."

    for voo in voos:
        if voo["id"] == id:
            voo["companhia"] = companhia
            voo["origem"] = origem
            voo["id_destino"] = id_destino
            voo["data_partida"] = data_partida
            voo["data_chegada"] = data_chegada
            voo["preco"] = preco
            return 200, voos

    return 404, "Voo não encontrado."


def remover_voo(id):
    if not voos:
        return 404, "Não existem voos registados."

    print("\n=== REMOVER VOO ===")
    for voo in voos:
        if voo["id"] == id:
            voos.remove(voo)
            return 200, voos

    return 404, "Voo não encontrado."

#############################################################################################

def validar_companhia(companhia):
    while not companhia.replace(" ", "").isalpha():
        companhia = input("Digite o nome da companhia aérea (apenas letras):")
    return companhia


def validar_origem(origem):
    while not origem.replace(" ", "").isalpha():
        origem = input("Digite a cidade de origem (apenas letras):")
    return origem


def validar_preco_voo(preco):
    while not preco.isdigit():
        preco = input("Digite o preço do voo (apenas números):")
    return preco
