from utils import validar_data, validar_nome, validar_nacionalidade, validar_telefone, validar_email, validar_NIF, validar_interesses, validar_orcamento, isEqual

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


def consultar_viajantes():
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    print("\n=== CONSULTAR VIAJANTE ===")
    nome = input("Nome do viajante para consultar: ").strip()

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
    return 200, "Sucesso"


def atualizar_viajantes():
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    print("\n=== ATUALIZAR VIAJANTE ===")
    nome = input("Digite o nome para atualizar o viajante: ").strip()

    if not nome:
        return 400, "Viajante não encontrado."

    for viajante in viajantes:
        if nome.lower() in viajante["nome"].lower():
            print("Digite os novos dados")

            novo_nome = input("Digite o novo nome:")
            nova_data = input("Digite a nova data de nascimento(DD/MM/AAAA):")
            nova_nacionalidade = input("Digite a nova nacionalidade:")
            novo_telefone = input("Digite o novo telefone:")
            novo_email = input("Digite o novo email:")
            novo_NIF = input("Digite o novo NIF:")
            novos_interesses = input("Digite os novos interesses:")
            novo_orcamento = input("Digite o novo orçamento(€):")

            viajante["nome"] = validar_nome(novo_nome)
            viajante["data_nascimento"] = validar_data(nova_data)
            viajante["nacionalidade"] = validar_nacionalidade(nova_nacionalidade)
            viajante["telefone"] = validar_telefone(novo_telefone)
            viajante["email"] = validar_email(novo_email)
            viajante["NIF"] = validar_NIF(novo_NIF)
            viajante["interesses"] = validar_interesses(novos_interesses)
            viajante["orcamento"] = validar_orcamento(novo_orcamento)

            return 200, "Sucesso"
    return 404, "Utilizador não encontrado."


def remover_viajantes():
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    print("\n=== REMOVER VIAJANTE ===")
    nome_remover = input("Nome do viajante para remover: ")

    for viajante in viajantes:
        if isEqual(nome_remover, viajante["nome"]):
            viajantes.remove(viajante)
            return 200, "Sucesso"

    return 404, "Utilizador não encontrado"
