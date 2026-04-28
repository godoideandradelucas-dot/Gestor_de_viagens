destinos = []
_proximo_id_destino = 1


def adicionar_destino(pais, cidade, tipo, atracoes):
    global _proximo_id_destino
    destino = {
        "id": _proximo_id_destino,
        "pais": pais,
        "cidade": cidade,
        "tipo": tipo,
        "atracoes": atracoes,
    }
    _proximo_id_destino += 1
    destinos.append(destino)
    return 201, "Destino criado com sucesso"


def ver_destinos():
    if not destinos:
        return 404, "Não existem destinos registados."
    return 200, destinos


def consultar_destinos(id):
    if not destinos:
        return 404, "Não existem destinos registados."

    print("\n=== CONSULTAR DESTINO ===")
    for destino in destinos:
        if destino["id"] == id:
            for chave, valor in destino.items():
                print(chave, ":", valor)
            print()
            return 200, "Destino encontrado"

    return 404, "Destino não encontrado."


def atualizar_destino(id, pais, cidade, tipo, atracoes):
    if not destinos:
        return 404, "Não existem destinos registados."

    for destino in destinos:
        if destino["id"] == id:
            destino["pais"] = pais
            destino["cidade"] = cidade
            destino["tipo"] = tipo
            destino["atracoes"] = atracoes
            return 200, "Destino atualizado"

    return 404, "Destino não encontrado."


def remover_destino(id):
    if not destinos:
        return 404, "Não existem destinos registados."

    print("\n=== REMOVER DESTINO ===")
    for destino in destinos:
        if destino["id"] == id:
            destinos.remove(destino)
            return 200, "Destino removido"

    return 404, "Destino não encontrado"

#############################################################################################

def validar_pais(pais):
    while not pais.replace(" ", "").isalpha():
        pais = input("Digite o nome do país(apenas letras):")
    return pais


def validar_cidade(cidade):
    while not cidade.replace(" ", "").isalpha():
        cidade = input("Digite o nome da cidade(apenas letras):")
    return cidade


def validar_tipo(tipo):
    while not tipo.replace(" ", "").isalpha():
        tipo = input("Digite o tipo de destino(apenas letras):")
    return tipo


def validar_atracoes(atracoes):
    while not atracoes.replace(" ", "").replace(",", "").isalpha():
        atracoes = input("Digite as atrações principais(apenas letras e vírgulas):")
    return atracoes
