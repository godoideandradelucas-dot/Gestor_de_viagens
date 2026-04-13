from utils import validar_data, validar_nome, validar_nacionalidade, validar_telefone, validar_email, validar_NIF, validar_interesses, validar_orcamento, isEqual

viajantes = []


def adicionar_viajante():
    print("\n=== CADASTRAR VIAJANTE ===")

    nome = validar_nome()
    data_nascimento = validar_data()
    nacionalidade = validar_nacionalidade()
    telefone = validar_telefone()
    email = validar_email()
    NIF = validar_NIF()
    interesses = validar_interesses()
    orcamento = validar_orcamento()

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
    return 201, "Sucesso"


def ver_viajantes():
    if not viajantes:
        return 404, "Não existem utilizadores registados."

    print("\n=== LISTA DE VIAJANTES ===")
    for viajante in viajantes:
        for chave, valor in viajante.items():
            print(chave,":",valor,)
        print()
    return 200, "Sucesso"


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
                print(chave,":",valor)
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

            viajante["nome"] = validar_nome()
            viajante["data_nascimento"] = validar_data()
            viajante["nacionalidade"] = validar_nacionalidade()
            viajante["telefone"] = validar_telefone()
            viajante["email"] = validar_email()
            viajante["NIF"] = validar_NIF()
            viajante["interesses"] = validar_interesses()
            viajante["orcamento"] = validar_orcamento()

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
