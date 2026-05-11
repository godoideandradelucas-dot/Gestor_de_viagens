import json
import os

FICHEIRO = "dados_destinos.json"

def _carregar():
    global destinos, _proximo_id_destino
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            dados = json.load(f)
        destinos = dados.get("lista", [])
        _proximo_id_destino = dados.get("proximo_id", 1)
    else:
        destinos = []
        _proximo_id_destino = 1

def _guardar():
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump({"lista": destinos, "proximo_id": _proximo_id_destino}, f, ensure_ascii=False, indent=2)

destinos = []
_proximo_id_destino = 1
_carregar()


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
    _guardar()
    return 201, destino


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
            return 200, destino

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
            _guardar()
            return 200, destinos

    return 404, "Destino não encontrado."


def remover_destino(id):
    if not destinos:
        return 404, "Não existem destinos registados."

    print("\n=== REMOVER DESTINO ===")
    for destino in destinos:
        if destino["id"] == id:
            destinos.remove(destino)
            _guardar()
            return 200, destinos

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
