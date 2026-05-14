import json
import os
from utils import isEqual

FICHEIRO = "dados_viajantes.json"

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
    return 201, viajante


def ver_viajantes():
    _carregar()
    if not viajantes:
        return 404, "Não existem utilizadores registados."
    return 200, viajantes


def consultar_viajantes(nome):
    _carregar()
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    if not nome:
        return 400, "Viajante não encontrado."

    for viajante in viajantes:
        if nome.lower() in viajante["nome"].lower():
            return 200, viajante
    return 404, "Viajante não encontrado."

def atualizar_viajantes(nome_procurar, nome, data_nascimento, nacionalidade, telefone, email, NIF, interesses, orcamento):
    _carregar()
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    if not nome_procurar:
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
            return 200, viajantes
    return 404, "Utilizador não encontrado."


def remover_viajantes(nome_remover):
    _carregar()
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    print("\n=== REMOVER VIAJANTE ===")
    for viajante in viajantes:
        if isEqual(nome_remover, viajante["nome"]):
            viajantes.remove(viajante)
            _guardar()
            return 200, viajantes
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
