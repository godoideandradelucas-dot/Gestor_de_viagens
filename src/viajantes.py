import json
import os
from utils import isEqual, get_logger

FICHEIRO = "dados_viajantes.json"
log = get_logger("viajantes")

def _carregar():
    global viajantes
    if os.path.exists(FICHEIRO):
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            dados = json.load(f)
        viajantes = dados.get("lista", [])
    else:
        viajantes = []

def _guardar():
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump({"lista": viajantes}, f, ensure_ascii=False, indent=2)

viajantes = []


def adicionar_viajante(nome, data_nascimento, nacionalidade, telefone, email, NIF, interesses, orcamento):
    _carregar()
    viajante = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "nacionalidade": nacionalidade,
        "telefone": telefone,
        "email": email,
        "NIF": NIF,
        "interesses": interesses,
        "orcamento": orcamento
    }
    viajantes.append(viajante)
    _guardar()
    log.info(f"Viajante adicionado: nome={nome}, NIF={NIF}, email={email}.")
    return 201, viajante


def ver_viajantes():
    _carregar()
    if not viajantes:
        log.error("Tentativa de listar viajantes: nenhum viajante registado.")
        return 404, "Não existem utilizadores registados."
    log.info(f"Listagem de viajantes: {len(viajantes)} viajante(s) encontrado(s).")
    return 200, viajantes


def consultar_viajantes(nome):
    _carregar()
    if not viajantes:
        log.error("Tentativa de consultar viajante: nenhum viajante registado.")
        return 404, "Não existem utilizadores registados."

    if not nome:
        log.error("Tentativa de consultar viajante com nome vazio.")
        return 400, "Viajante não encontrado."

    for viajante in viajantes:
        if nome.lower() in viajante["nome"].lower():
            log.info(f"Viajante consultado: nome={viajante['nome']}.")
            return 200, viajante

    log.error(f"Viajante não encontrado: nome={nome}.")
    return 404, "Viajante não encontrado."

def atualizar_viajantes(nome_procurar, nome, data_nascimento, nacionalidade, telefone, email, NIF, interesses, orcamento):
    _carregar()
    if not viajantes:
        log.error("Tentativa de atualizar viajante: nenhum viajante registado.")
        return 404, "Não existem utilizadores registados."

    if not nome_procurar:
        log.error("Tentativa de atualizar viajante com nome vazio.")
        return 400, "Viajante não encontrado."

    for viajante in viajantes:
        if nome_procurar.lower() in viajante["nome"].lower():
            viajante["nome"] = nome
            viajante["data_nascimento"] = data_nascimento
            viajante["nacionalidade"] = nacionalidade
            viajante["telefone"] = telefone
            viajante["email"] = email
            viajante["NIF"] = NIF
            viajante["interesses"] = interesses
            viajante["orcamento"] = orcamento
            _guardar()
            log.info(f"Viajante atualizado: nome anterior={nome_procurar}, novo nome={nome}, NIF={NIF}.")
            return 200, viajantes

    log.error(f"Tentativa de atualizar viajante não encontrado: nome={nome_procurar}.")
    return 404, "Utilizador não encontrado."


def remover_viajantes(nome_remover):
    _carregar()
    if not viajantes:
        log.error("Tentativa de remover viajante: nenhum viajante registado.")
        return 404, "Não existem utilizadores registados."

    print("\n=== REMOVER VIAJANTE ===")
    for viajante in viajantes:
        if isEqual(nome_remover, viajante["nome"]):
            viajantes.remove(viajante)
            _guardar()
            log.info(f"Viajante removido: nome={nome_remover}.")
            return 200, viajantes

    log.error(f"Tentativa de remover viajante não encontrado: nome={nome_remover}.")
    return 404, "Utilizador não encontrado"

############################################################################################

def validar_nome(nome):
    while not nome.replace(" ", "").isalpha():
        nome = input("Digite seu nome(apenas letras):")
    return nome

def validar_nacionalidade(nacionalidade):
    while not nacionalidade.replace(" ", "").isalpha():
        nacionalidade = input("Digite sua nacionalidade(apenas letras):")
    return nacionalidade


def validar_interesses(interesses):
    while not interesses.replace(" ", "").replace(",", "").isalpha():
        interesses = input("Digite seus interesses(ex: praias, natureza, montanhas):")
    return interesses


def validar_orcamento(orcamento):
    while not orcamento.isdigit():
        orcamento = input("Digite seu orçamento(apenas numeros):")
    return orcamento
