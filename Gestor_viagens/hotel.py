from trabalhos_PSI.Gestor_viagens.utils import validar_hotel, validar_local, validar_preco, validar_tipo_hotel, verificar_hoteis

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
    print("Hotel adicionado com sucesso!\n")


def ver_hoteis():
    if not verificar_hoteis(hoteis):
        return

    print("\n=== LISTA DE HOTÉIS ===")
    for hotel in hoteis:
        for chave, valor in hotel.items():
            print(chave,":",valor)
        print()


def consultar_hotel():
    if not verificar_hoteis(hoteis):
        return

    print("\n=== CONSULTAR HOTEL ===")
    nome = input("Nome do hotel para consultar:")
    for hotel in hoteis:
        if nome.lower() in hotel["nome"].lower():
            for chave, valor in hotel.items():
                print(chave,":",valor)


def atualizar_hotel():
    if not verificar_hoteis(hoteis):
        return

    print("\n=== ATUALIZAR HOTEL ===")
    nome = input("Digite o nome do hotel para atualizar:")
    for hotel in hoteis:
        if nome.lower() in hotel["nome"].lower():
            print("Digite os novos dados")

            hotel["nome"] = validar_hotel()
            hotel["local"] = validar_local()
            hotel["preco"] = validar_preco()
            hotel["tipo"] = validar_tipo_hotel()

            print("hotel atualizado!\n")
            return


def remover_hotel():
    if not verificar_hoteis(hoteis):
        return

    print("\n=== REMOVER HOTEL ===")
    nome_remover = input("Digite o nome do hotel para remover:")
    for hotel in hoteis:
        if nome_remover.lower() == hotel["nome"].lower():
            hoteis.remove(hotel)
            print("hotel removido com sucesso!")
            return
    print("Hotel não encontrado.\n")
