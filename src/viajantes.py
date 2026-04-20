from utils import isEqual

viajantes = []

def adicionar_viajante(nome, data_nascimento, nacionalidade, telefone, email, NIF, interesses, orcamento):
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
    return 201, viajante


def ver_viajantes():
    if not viajantes:
        return 404, "Não existem utilizadores registados."
    return 200, viajantes


def consultar_viajantes(nome):
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    print("\n=== CONSULTAR VIAJANTE ===")
    if not nome:
        return 400, "Viajante não encontrado."

    encontrado = False
    for viajante in viajantes:
        if nome.lower() in viajante["nome"].lower():
            for chave, valor in viajante.items():
                print(chave, ":", valor)
            print()
            encontrado = True

    if not encontrado:
        return 404, "Viajante não encontrado."
    return 200, "Viajante encontrado"

def atualizar_viajantes(nome_procurar, nome, data_nascimento, nacionalidade, telefone, email, NIF, interesses, orcamento):
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
            return 200, "Viajante atualizado"
    return 404, "Utilizador não encontrado."


def remover_viajantes(nome_remover):
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    print("\n=== REMOVER VIAJANTE ===")
    for viajante in viajantes:
        if isEqual(nome_remover, viajante["nome"]):
            viajantes.remove(viajante)
            return 200, "Viajante Removido"
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
