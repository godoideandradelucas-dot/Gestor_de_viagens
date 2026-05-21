import json
import os
from utils import get_logger

FICHEIRO = "dados_voos.json"
log = get_logger("voo")

def _carregar():
    global voos, _proximo_id_voo
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            dados = json.load(f)
        voos = dados.get("lista", [])
        _proximo_id_voo = dados.get("proximo_id", 1)
    else:
        voos = []
        _proximo_id_voo = 1

def _guardar():
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump({"lista": voos, "proximo_id": _proximo_id_voo}, f, ensure_ascii=False, indent=2)

voos = []
_proximo_id_voo = 1


def adicionar_voo(companhia, origem, id_destino, data_partida, data_chegada, preco):
    global _proximo_id_voo
    _carregar()
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
    _guardar()
    log.info(f"Voo adicionado: id={voo['id']}, companhia={companhia}, origem={origem}, destino_id={id_destino}, partida={data_partida}.")
    return 201, voo


def ver_voos():
    _carregar()
    if not voos:
        log.warning("Tentativa de listar voos: nenhum voo registado.")
        return 404, "Não existem voos registados."
    log.info(f"Listagem de voos: {len(voos)} voo(s) encontrado(s).")
    return 200, voos


def consultar_voo(id):
    _carregar()
    if not voos:
        log.warning("Tentativa de consultar voo: nenhum voo registado.")
        return 404, "Não existem voos registados."

    print("\n=== CONSULTAR VOO ===")
    for voo in voos:
        if voo["id"] == id:
            log.info(f"Voo consultado: id={id}, companhia={voo['companhia']}.")
            return 200, voo

    log.warning(f"Voo não encontrado: id={id}.")
    return 404, "Voo não encontrado."


def atualizar_voo(id, companhia, origem, id_destino, data_partida, data_chegada, preco):
    _carregar()
    if not voos:
        log.warning("Tentativa de atualizar voo: nenhum voo registado.")
        return 404, "Não existem voos registados."

    for voo in voos:
        if voo["id"] == id:
            voo["companhia"] = companhia
            voo["origem"] = origem
            voo["id_destino"] = id_destino
            voo["data_partida"] = data_partida
            voo["data_chegada"] = data_chegada
            voo["preco"] = preco
            _guardar()
            log.info(f"Voo atualizado: id={id}, nova companhia={companhia}, nova origem={origem}.")
            return 200, voos

    log.warning(f"Tentativa de atualizar voo não encontrado: id={id}.")
    return 404, "Voo não encontrado."


def remover_voo(id):
    _carregar()
    if not voos:
        log.warning("Tentativa de remover voo: nenhum voo registado.")
        return 404, "Não existem voos registados."

    print("\n=== REMOVER VOO ===")
    for voo in voos:
        if voo["id"] == id:
            voos.remove(voo)
            _guardar()
            log.info(f"Voo removido: id={id}.")
            return 200, voos

    log.warning(f"Tentativa de remover voo não encontrado: id={id}.")
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
