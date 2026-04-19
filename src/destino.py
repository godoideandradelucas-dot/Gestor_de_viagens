from utils import isEqual

destinos = []

def adicionar_destino(pais, cidade, tipo, atracoes):
    destino = {
        "pais": pais,
        "cidade": cidade,
        "tipo": tipo,
        "atracoes": atracoes,
    }
    destinos.append(destino)
    return 201, "Sucesso"


def ver_destinos():
    if not destinos:
        return 404, "Não existem destinos registados."
    return 200, destinos


def consultar_destinos():
    if not destinos:
        return 404, "Não existem destinos registados."

    print("\n=== CONSULTAR DESTINO ===")
    nome = input("Nome do destino para consultar:").strip()
    if not nome:
        return 400, "Destino não encontrado."

    encontrado = False
    for destino in destinos:
        if nome.lower() in destino["pais"].lower():
            for chave, valor in destino.items():
                print(chave, ":", valor)
            print()
            encontrado = True

    if not encontrado:
        return 404, "Destino não encontrado."
    return 200, "Sucesso"


def atualizar_destino(nome_procurar, pais, cidade, tipo, atracoes):
    if not destinos:
        return 404, "Não existem destinos registados."

    nome = input("Digite o nome para atualizar o destino:").strip()
    if not nome:
        return 400, "Destino não encontrado."

    for destino in destinos:
        if nome_procurar.lower() in destino["pais"].lower():
            destino["pais"] = pais
            destino["cidade"] = cidade
            destino["tipo"] = tipo
            destino["atracoes"] = atracoes
            return 200, "Sucesso"
    return 404, "Destino não encontrado."


def remover_destino():
    if not destinos:
        return 404, "Não existem destinos registados."

    print("\n=== REMOVER DESTINO ===")
    nome_remover = input("Digite o nome do destino para remover:")
    for destino in destinos:
        if isEqual(nome_remover, destino["pais"]):
            destinos.remove(destino)
            return 200, "Sucesso"
    return 404, "Destino não encontrado"
