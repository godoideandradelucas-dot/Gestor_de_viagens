import json
import os
from utils import get_logger

FICHEIRO = "dados_hoteis.json"
log = get_logger("hotel")

def _carregar():
    global hoteis, _proximo_id_hotel
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            dados = json.load(f)
        hoteis = dados.get("lista", [])
        _proximo_id_hotel = dados.get("proximo_id", 1)
    else:
        hoteis = []
        _proximo_id_hotel = 1

def _guardar():
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump({"lista": hoteis, "proximo_id": _proximo_id_hotel}, f, ensure_ascii=False, indent=2)

hoteis = []
_proximo_id_hotel = 1


def adicionar_hotel(nome_hotel, local, preco, tipo_hotel):
    global _proximo_id_hotel
    _carregar()
    hotel = {
        "id": _proximo_id_hotel,
        "nome": nome_hotel,
        "local": local,
        "preco": preco,
        "tipo": tipo_hotel,
    }
    _proximo_id_hotel += 1
    hoteis.append(hotel)
    _guardar()
    log.info(f"Hotel adicionado: id={hotel['id']}, nome={nome_hotel}, local={local}, tipo={tipo_hotel}.")
    return 201, hotel


def ver_hoteis():
    _carregar()
    if not hoteis:
        log.error("Tentativa de listar hoteis: nenhum hotel registado.")
        return 404, "Não existem hoteis registados."
    log.info(f"Listagem de hoteis: {len(hoteis)} hotel(is) encontrado(s).")
    return 200, hoteis


def consultar_hotel(id):
    _carregar()
    if not hoteis:
        log.error("Tentativa de consultar hotel: nenhum hotel registado.")
        return 404, "Não existem hoteis registados."

    print("\n=== CONSULTAR HOTEL ===")
    for hotel in hoteis:
        if hotel["id"] == id:
            log.info(f"Hotel consultado: id={id}, nome={hotel['nome']}.")
            return 200, hotel

    log.error(f"Hotel não encontrado: id={id}.")
    return 404, "Hotel não encontrado."


def atualizar_hotel(id, nome_hotel, local, preco, tipo_hotel):
    _carregar()
    if not hoteis:
        log.error("Tentativa de atualizar hotel: nenhum hotel registado.")
        return 404, "Não existem hoteis registados."

    for hotel in hoteis:
        if hotel["id"] == id:
            hotel["nome"] = nome_hotel
            hotel["local"] = local
            hotel["preco"] = preco
            hotel["tipo"] = tipo_hotel
            _guardar()
            log.info(f"Hotel atualizado: id={id}, novo nome={nome_hotel}, novo local={local}.")
            return 200, hoteis

    log.error(f"Tentativa de atualizar hotel não encontrado: id={id}.")
    return 404, hoteis


def remover_hotel(id):
    _carregar()
    if not hoteis:
        log.error("Tentativa de remover hotel: nenhum hotel registado.")
        return 404, "Não existem hoteis registados."

    print("\n=== REMOVER HOTEL ===")
    for hotel in hoteis:
        if hotel["id"] == id:
            hoteis.remove(hotel)
            _guardar()
            log.info(f"Hotel removido: id={id}.")
            return 200, hoteis

    log.error(f"Tentativa de remover hotel não encontrado: id={id}.")
    return 404, "Hotel não encontrado."

#############################################################################################

def validar_hotel(nome_hotel):
    while not nome_hotel.replace(" ", "").isalpha():
        nome_hotel = input("Digite o nome do hotel(apenas letras):")
    return nome_hotel


def validar_local(local):
    while not local.replace(" ", "").isalpha():
        local = input("Digite a localizacao(apenas letras):")
    return local


def validar_preco(preco):
    while not preco.isdigit():
        preco = input("Digite o preço por noite(apenas numeros):")
    return preco


def validar_tipo_hotel(tipo_hotel):
    while not tipo_hotel.isalpha():
        tipo_hotel = input("Digite o tipo de hospedagem (hotel, pousada, resort):")
    return tipo_hotel
