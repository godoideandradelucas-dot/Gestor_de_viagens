from trabalhos_PSI.Gestor_viagens.utils import validar_pais, validar_cidade, validar_tipo, validar_atracoes, verificar_destinos

destinos = []

def adicionar_destino():
    print("\n=== ADICIONAR DESTINO ===")

    pais =  validar_pais()
    cidade = validar_cidade()
    tipo = validar_tipo()
    atracoes = validar_atracoes()

    destino = {
        "pais": pais,
        "cidade": cidade,
        "tipo": tipo,
        "atracoes": atracoes,
    }
    destinos.append(destino)
    print("Destino adicionado com sucesso!\n")


def ver_destinos():
    if not verificar_destinos(destinos):
        return

    print("\n=== LISTA DE DESTINOS ===")
    for destino in destinos:
        for chave, valor in destino.items():
            print(chave,":",valor)
        print()


def consultar_destinos():
    if not verificar_destinos(destinos):
        return

    print("\n=== CONSULTAR DESTINO ===")
    nome = input("Nome do destino para consultar:")
    for destino in destinos:
        if nome.lower() in destino["pais"].lower():
            for chave, valor in destino.items():
                print(chave,":",valor)


def atualizar_destino():
    if not verificar_destinos(destinos):
        return

    print("\n=== ATUALIZAR DESTINO ===")
    nome = input("Digite o nome para atualizar o destino:")
    for destino in destinos:
        if nome.lower() in destino["pais"].lower():
            print("Digite os novos dados")

            destino["pais"] = validar_pais()
            destino["cidade"] = validar_cidade()
            destino["tipo"] = validar_tipo()
            destino["atracoes"] = validar_atracoes()

            print("Destino atualizado com sucesso!\n")
            return


def remover_destino():
    if not verificar_destinos(destinos):
        return

    print("\n=== REMOVER DESTINO ===")
    nome_remover = input("Digite o nome do destino para remover:")
    for destino in destinos:
        if nome_remover.lower() == destino["pais"].lower():
            destinos.remove(destino)
            print("Destino removido com sucesso!")
            return

    print("Destino não encontrado.\n")
