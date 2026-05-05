viagens = []
_proximo_id_viagem = 1


def adicionar_viagem(id_voo_ida, id_voo_volta, lista_id_viajantes, id_hotel, id_destino):
    global _proximo_id_viagem
    viagem = {
        "id": _proximo_id_viagem,
        "id_voo_ida": id_voo_ida,
        "id_voo_volta": id_voo_volta,
        "lista_id_viajantes": lista_id_viajantes,
        "id_hotel": id_hotel,
        "id_destino": id_destino,
    }
    _proximo_id_viagem += 1
    viagens.append(viagem)
    return 201, viagem


def ver_viagens():
    if not viagens:
        return 404, "Não existem viagens registadas."
    return 200, viagens


def consultar_viagem(id):
    if not viagens:
        return 404, "Não existem viagens registadas."

    print("\n=== CONSULTAR VIAGEM ===")
    for viagem in viagens:
        if viagem["id"] == id:
            return 200, viagens

    return 404, "Viagem não encontrada."


def atualizar_viagem(id, id_voo_ida, id_voo_volta, lista_id_viajantes, id_hotel, id_destino):
    if not viagens:
        return 404, "Não existem viagens registadas."

    for viagem in viagens:
        if viagem["id"] == id:
            viagem["id_voo_ida"] = id_voo_ida
            viagem["id_voo_volta"] = id_voo_volta
            viagem["lista_id_viajantes"] = lista_id_viajantes
            viagem["id_hotel"] = id_hotel
            viagem["id_destino"] = id_destino
            return 200, viagens

    return 404, "Viagem não encontrada."


def remover_viagem(id):
    if not viagens:
        return 404, "Não existem viagens registadas."

    print("\n=== REMOVER VIAGEM ===")
    for viagem in viagens:
        if viagem["id"] == id:
            viagens.remove(viagem)
            return 200, viagens

    return 404, "Viagem não encontrada."

#############################################################################################

def validar_lista_nifs(lista_nifs_str):
    while True:
        nifs = [nif.strip() for nif in lista_nifs_str.split(",")]
        valido = True
        for nif in nifs:
            if not nif.isdigit() or len(nif) != 9:
                valido = False
                break
        if valido:
            return nifs

        print("Erro: cada NIF deve ter exatamente 9 dígitos numéricos.")
        lista_nifs_str = input("Digite os NIFs dos viajantes (9 dígitos, separados por vírgula): ")
