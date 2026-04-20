from destino import adicionar_destino, ver_destinos, consultar_destinos, atualizar_destino, remover_destino, destinos, validar_pais, validar_cidade, validar_tipo, validar_atracoes
from hotel import adicionar_hotel, ver_hoteis, consultar_hotel, atualizar_hotel, remover_hotel, hoteis, validar_hotel, validar_local, validar_preco, validar_tipo_hotel
from viajantes import adicionar_viajante, ver_viajantes, consultar_viajantes, atualizar_viajantes, remover_viajantes, viajantes, validar_nome, validar_nacionalidade, validar_interesses, validar_orcamento
from utils import validar_data, validar_telefone, validar_email, validar_NIF

def menu():
    while True:
        print("\n----------------------------- Gestor de Viagens -----------------------------")
        print("1 - Adicionar viajante     6 - Adicionar destino     11 - Adicionar hotel")
        print("2 - Ver viajantes          7 - Ver destinos          12 - Ver hoteis")
        print("3 - Consultar viajante     8 - Consultar destino     13 - Consultar hotel")
        print("4 - Atualizar viajante     9 - Atualizar destino     14 - Atualizar hotel")
        print("5 - Remover viajante       10 - Remover destino      15 - Remover hotel")
        print("")
        print("                                0 - sair")
        print("----------------------------------------------------------------------------")
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            print("\n=== CADASTRAR VIAJANTE ===")
            nome = input("Digite seu nome:")
            nome = validar_nome(nome)

            data_nascimento = input("Digite sua data de nascimento(DD/MM/AAAA):")
            data_nascimento = validar_data(data_nascimento)

            nacionalidade = input("Digite sua nacionalidade:")
            nacionalidade = validar_nacionalidade(nacionalidade)

            telefone = input("Digite seu telefone:")
            telefone = validar_telefone(telefone)

            email = input("Digite seu email(@gmail.com - @hotmail.com - @outlook.com):")
            email = validar_email(email)

            NIF = input("Digite seu NIF:")
            NIF = validar_NIF(NIF)

            interesses = input("Digite seus interesses(ex: praias, natureza, montanhas):")
            interesses = validar_interesses(interesses)

            orcamento = input("Digite seu orçamento(€):")
            orcamento = validar_orcamento(orcamento)

            return_code = adicionar_viajante(nome, data_nascimento, nacionalidade, telefone, email, NIF, interesses, orcamento)
            if return_code[0] == 201:
                print("Viajante criado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "2":
            return_code = ver_viajantes()
            if return_code[0] == 200:
                print("\n=== LISTA DE VIAJANTES ===")
                for viajante in return_code[1]:
                    for chave, valor in viajante.items():
                        print(chave, ":", valor)
                    print()
                print("Viajantes listados com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "3":
            nome = input("Nome do viajante para consultar: ").strip()
            return_code = consultar_viajantes(nome)
            if return_code[0] == 200:
                print("Viajante listado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "4":
            if not viajantes:
                print("Erro: Não existem utilizadores registados.")
            else:
                print("\n=== ATUALIZAR VIAJANTE ===")
                nome_procurar = input("Digite o nome do viajante para atualizar: ").strip()
                print("Digite os novos dados")
                nome = validar_nome(input("Digite o novo nome:"))
                data_nascimento = validar_data(input("Digite a nova data de nascimento(DD/MM/AAAA):"))
                nacionalidade = validar_nacionalidade(input("Digite a nova nacionalidade:"))
                telefone = validar_telefone(input("Digite o novo telefone:"))
                email = validar_email(input("Digite o novo email:"))
                NIF = validar_NIF(input("Digite o novo NIF:"))
                interesses = validar_interesses(input("Digite os novos interesses:"))
                orcamento = validar_orcamento(input("Digite o novo orçamento(€):"))
                return_code = atualizar_viajantes(nome_procurar, nome, data_nascimento, nacionalidade, telefone, email, NIF, interesses, orcamento)
                if return_code[0] == 200:
                    print("Viajante atualizado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "5":
            nome_remover = input("Nome do viajante para remover: ")
            return_code = remover_viajantes(nome_remover)
            if return_code[0] == 200:
                print("Viajante removido com sucesso.")
            else:
                print("Erro: " + return_code[1])

#############################################################################################

        elif opcao == "6":
            print("\n=== ADICIONAR DESTINO ===")
            pais = input("Digite o nome do país:")
            pais = validar_pais(pais)

            cidade = input("Digite o nome da cidade:")
            cidade = validar_cidade(cidade)

            tipo = input("Digite o tipo de destino (praia, urbano, montanha, natureza):")
            tipo = validar_tipo(tipo)

            atracoes = input("Digite as atrações principais(ex: museus, praias, castelos):")
            atracoes = validar_atracoes(atracoes)

            return_code = adicionar_destino(pais, cidade, tipo, atracoes)
            if return_code[0] == 201:
                print("Destino criado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "7":
            return_code = ver_destinos()
            if return_code[0] == 200:
                print("\n=== LISTA DE DESTINOS ===")
                for destino in return_code[1]:
                    for chave, valor in destino.items():
                        print(chave, ":", valor)
                    print()
                print("Destinos listados com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "8":
            nome = input("Nome do destino para consultar:").strip()
            return_code = consultar_destinos(nome)
            if return_code[0] == 200:
                print("Destino listado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "9":
            if not destinos:
                print("Erro: Não existem destinos registados.")
            else:
                print("\n=== ATUALIZAR DESTINO ===")
                nome_procurar = input("Digite o nome do destino para atualizar: ").strip()
                print("Digite os novos dados")
                pais = validar_pais(input("Digite o novo país: "))
                cidade = validar_cidade(input("Digite a nova cidade: "))
                tipo = validar_tipo(input("Digite o novo tipo: "))
                atracoes = validar_atracoes(input("Digite as novas atrações: "))
                return_code = atualizar_destino(nome_procurar, pais, cidade, tipo, atracoes)
                if return_code[0] == 200:
                    print("Destino atualizado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "10":
            nome_remover = input("Digite o nome do destino para remover:")
            return_code = remover_destino(nome_remover)
            if return_code[0] == 200:
                print("Destino removido com sucesso.")
            else:
                print("Erro: " + return_code[1])

#############################################################################################

        elif opcao == "11":
            print("\n=== ADICIONAR HOTEL ===")
            nome_hotel = input("Digite o nome do hotel:")
            nome_hotel = validar_hotel(nome_hotel)

            local = input("Digite a localizacao(cidade):")
            local = validar_local(local)

            preco = input("Digite o preço por noite(€):")
            preco = validar_preco(preco)

            tipo_hotel = input("Digite o tipo de hospedagem (hotel, pousada, resort):")
            tipo_hotel = validar_tipo_hotel(tipo_hotel)

            return_code = adicionar_hotel(nome_hotel, local, preco, tipo_hotel)
            if return_code[0] == 201:
                print("Hotel criado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "12":
            return_code = ver_hoteis()
            if return_code[0] == 200:
                print("\n=== LISTA DE HOTÉIS ===")
                for hotel in return_code[1]:
                    for chave, valor in hotel.items():
                        print(chave, ":", valor)
                    print()
                print("Hoteis listados com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "13":
            nome = input("Nome do hotel para consultar:").strip()
            return_code = consultar_hotel(nome)
            if return_code[0] == 200:
                print("Hotel listado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "14":
            if not hoteis:
                print("Erro: Não existem hoteis registados.")
            else:
                print("\n=== ATUALIZAR HOTEL ===")
                nome_procurar = input("Digite o nome do hotel para atualizar: ").strip()
                print("Digite os novos dados")
                nome_hotel = validar_hotel(input("Digite o novo nome do hotel:"))
                local = validar_local(input("Digite a nova localizacao(cidade):"))
                preco = validar_preco(input("Digite o novo preço por noite(€):"))
                tipo_hotel = validar_tipo_hotel(input("Digite o novo tipo de hospedagem (hotel, pousada, resort):"))
                return_code = atualizar_hotel(nome_procurar, nome_hotel, local, preco, tipo_hotel)
                if return_code[0] == 200:
                    print("Hotel atualizado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "15":
            nome_remover = input("Digite o nome do hotel para remover:")
            return_code = remover_hotel(nome_remover)
            if return_code[0] == 200:
                print("Hotel removido com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    menu()
