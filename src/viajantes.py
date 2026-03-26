from trabalhos_PSI.src.utils import validar_data, validar_nome, validar_nacionalidade, validar_telefone, validar_email, validar_NIF, validar_interesses, validar_orcamento, verificar_viajantes

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
    print("Viajante cadastrado com sucesso!\n")


def ver_viajantes():
    if not verificar_viajantes(viajantes):
        return

    print("\n=== LISTA DE VIAJANTES ===")
    for viajante in viajantes:
        for chave, valor in viajante.items():
            print(chave,":",valor,)
        print()


def consultar_viajantes():
    if not verificar_viajantes(viajantes):
        return

    print("\n=== CONSULTAR VIAJANTE ===")
    nome = input("Nome do viajante para consultar: ")
    for viajante in viajantes:
        if nome.lower() in viajante["nome"].lower():
            for chave, valor in viajante.items():
                print(chave,":",valor)


def atualizar_viajantes():
    if not verificar_viajantes(viajantes):
        return

    print("\n=== ATUALIZAR VIAJANTE ===")
    nome = input("Digite o nome para atualizar o viajante: ")
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

            print("Viajante atualizado com sucesso!\n")
            return


def remover_viajantes():
    if not verificar_viajantes(viajantes):
        return

    print("\n=== REMOVER VIAJANTE ===")
    nome_remover = input("Nome do viajante para remover:")
    for viajante in viajantes:
        if nome_remover.lower() == viajante["nome"].lower():
            viajantes.remove(viajante)
            print("Viajante removido com sucesso!")
            return

    print("Viajante não encontrado.\n")