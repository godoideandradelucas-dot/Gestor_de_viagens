import json
import os
from utils import get_logger

FICHEIRO = "dados_destinos.json"
log = get_logger("destino")

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


def adicionar_destino(pais, cidade, tipo, atracoes):
    global _proximo_id_destino
    _carregar()
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
    log.info(f"Destino adicionado: id={destino['id']}, cidade={cidade}, pais={pais}, tipo={tipo}")
    return 201, destino


def ver_destinos():
    _carregar()
    if not destinos:
        log.warning("Tentativa de listar destinos: nenhum destino registado.")
        return 404, "Não existem destinos registados."
    log.info(f"Listagem de destinos: {len(destinos)} destino(s) encontrado(s).")
    return 200, destinos


def consultar_destinos(id):
    _carregar()
    if not destinos:
        log.warning("Tentativa de consultar destino: nenhum destino registado.")
        return 404, "Não existem destinos registados."

    print("\n=== CONSULTAR DESTINO ===")
    for destino in destinos:
        if destino["id"] == id:
            log.info(f"Destino consultado: id={id}, cidade={destino['cidade']}.")
            return 200, destino

    log.warning(f"Destino não encontrado: id={id}.")
    return 404, "Destino não encontrado."


def atualizar_destino(id, pais, cidade, tipo, atracoes):
    _carregar()
    if not destinos:
        log.warning("Tentativa de atualizar destino: nenhum destino registado.")
        return 404, "Não existem destinos registados."

    for destino in destinos:
        if destino["id"] == id:
            destino["pais"] = pais
            destino["cidade"] = cidade
            destino["tipo"] = tipo
            destino["atracoes"] = atracoes
            _guardar()
            log.info(f"Destino atualizado: id={id}, nova cidade={cidade}, novo pais={pais}.")
            return 200, destinos

    log.warning(f"Tentativa de atualizar destino não encontrado: id={id}.")
    return 404, "Destino não encontrado."


def remover_destino(id):
    _carregar()
    if not destinos:
        log.warning("Tentativa de remover destino: nenhum destino registado.")
        return 404, "Não existem destinos registados."

    print("\n=== REMOVER DESTINO ===")
    for destino in destinos:
        if destino["id"] == id:
            destinos.remove(destino)
            _guardar()
            log.info(f"Destino removido: id={id}.")
            return 200, destinos

    log.warning(f"Tentativa de remover destino não encontrado: id={id}.")
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
