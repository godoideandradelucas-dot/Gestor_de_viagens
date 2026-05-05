from datetime import datetime

def isEqual(nome_1, nome_2):
    return nome_1.lower() == nome_2.lower()

def validar_id(mensagem):
    while True:
        valor = input(mensagem)
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Erro: introduza um ID válido (número inteiro positivo).")

def validar_data(data_nascimento):
    while True:
        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")
            return data_nascimento
        except ValueError:
            print("Erro: data inválida! Use o formato DD/MM/AAAA")
            data_nascimento = input("Digite sua data de nascimento(DD/MM/AAAA):")


def validar_telefone(telefone):
    while not (telefone.isdigit() and len(telefone) == 9):
        print("Erro: o número deve ter 9 dígitos e só números!")
        telefone = input("Digite novamente: ")
    return telefone


def validar_email(email):
    while not ("@gmail.com" in email or "@hotmail.com" in email or "@outlook.com" in email):
        print("Erro: email inválido!")
        email = input("Digite seu email novamente (@gmail.com - @hotmail.com - @outlook.com): ")
    return email


def validar_NIF(NIF):
    while not (NIF.isdigit() and len(NIF) == 9):
        print("Erro: o NIF deve ter 9 números!")
        NIF = input("Digite seu NIF novamente: ")
    return NIF



def validar_id_destino(mensagem, destinos):
    if not destinos:
        return None, "Não existem destinos registados."
    ids_disponiveis = []
    for destino in destinos:
        ids_disponiveis.append(str(destino["id"]))
    while True:
        id = validar_id(mensagem)
        encontrado = False
        for destino in destinos:
            if destino["id"] == id:
                encontrado = True
                break
        if encontrado:
            return id, None
        print("Erro: destino com esse ID não existe. IDs disponíveis: " + ", ".join(ids_disponiveis))


def validar_id_hotel(mensagem, hoteis):
    if not hoteis:
        return None, "Não existem hoteis registados."
    ids_disponiveis = []
    for hotel in hoteis:
        ids_disponiveis.append(str(hotel["id"]))
    while True:
        id = validar_id(mensagem)
        encontrado = False
        for hotel in hoteis:
            if hotel["id"] == id:
                encontrado = True
                break
        if encontrado:
            return id, None
        print("Erro: hotel com esse ID não existe. IDs disponíveis: " + ", ".join(ids_disponiveis))


def validar_id_voo(mensagem, voos):
    if not voos:
        return None, "Não existem voos registados."
    ids_disponiveis = []
    for voo in voos:
        ids_disponiveis.append(str(voo["id"]))
    while True:
        id = validar_id(mensagem)
        encontrado = False
        for voo in voos:
            if voo["id"] == id:
                encontrado = True
                break
        if encontrado:
            return id, None
        print("Erro: voo com esse ID não existe. IDs disponíveis: " + ", ".join(ids_disponiveis))


def validar_id_voo_volta(mensagem, voos):
    if not voos:
        return None, "Não existem voos registados."
    ids_disponiveis = []
    for voo in voos:
        ids_disponiveis.append(str(voo["id"]))
    resposta = input("A viagem tem voo de volta? (s/n): ").strip().lower()
    while resposta != "s" and resposta != "n":
        print("Erro: responda apenas s ou n.")
        resposta = input("A viagem tem voo de volta? (s/n): ").strip().lower()
    if resposta == "n":
        return None, None
    while True:
        id = validar_id(mensagem)
        encontrado = False
        for voo in voos:
            if voo["id"] == id:
                encontrado = True
                break
        if encontrado:
            return id, None
        print("Erro: voo com esse ID não existe. IDs disponíveis: " + ", ".join(ids_disponiveis))


def mostrar_destinos_disponiveis(destinos):
    info = ", ".join(str(d["id"]) + " - " + d["cidade"] for d in destinos)
    print("Destinos disponíveis: " + info)


def mostrar_hoteis_disponiveis(hoteis):
    info = ", ".join(str(h["id"]) + " - " + h["nome"] for h in hoteis)
    print("Hotéis disponíveis: " + info)


def mostrar_voos_disponiveis(voos):
    info = ", ".join(str(v["id"]) + " - " + v["companhia"] + " (" + v["origem"] + ")" for v in voos)
    print("Voos disponíveis: " + info)


def mostrar_viagens_disponiveis(viagens):
    info = ", ".join(str(v["id"]) for v in viagens)
    print("Viagens disponíveis: " + info)


def mostrar_nifs_disponiveis(viajantes):
    info = ", ".join(v["NIF"] + " (" + v["nome"] + ")" for v in viajantes)
    print("NIFs disponíveis: " + info)
