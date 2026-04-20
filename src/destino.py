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
    return 201, "Destino criado com sucesso"


def ver_destinos():
    if not destinos:
        return 404, "Não existem destinos registados."
    return 200, destinos


def consultar_destinos(nome):
    if not destinos:
        return 404, "Não existem destinos registados."

    print("\n=== CONSULTAR DESTINO ===")
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
    return 200, "Destino encontrado"


def atualizar_destino(nome_procurar, pais, cidade, tipo, atracoes):
    if not destinos:
        return 404, "Não existem destinos registados."

    if not nome_procurar:
        return 400, "Destino não encontrado."

    for destino in destinos:
        if nome_procurar.lower() in destino["pais"].lower():
            destino["pais"] = pais
            destino["cidade"] = cidade
            destino["tipo"] = tipo
            destino["atracoes"] = atracoes
            return 200, "Destino atualizado"
    return 404, "Destino não encontrado."


def remover_destino(nome_remover):
    if not destinos:
        return 404, "Não existem destinos registados."

    print("\n=== REMOVER DESTINO ===")
    for destino in destinos:
        if isEqual(nome_remover, destino["pais"]):
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
