from destino import adicionar_destino, ver_destinos, consultar_destinos, atualizar_destino, remover_destino, destinos, validar_pais, validar_cidade, validar_tipo, validar_atracoes
from hotel import adicionar_hotel, ver_hoteis, consultar_hotel, atualizar_hotel, remover_hotel, hoteis, validar_hotel, validar_local, validar_preco, validar_tipo_hotel
from viajantes import adicionar_viajante, ver_viajantes, consultar_viajantes, atualizar_viajantes, remover_viajantes, viajantes, validar_nome, validar_nacionalidade, validar_interesses, validar_orcamento
from voo import adicionar_voo, ver_voos, consultar_voo, atualizar_voo, remover_voo, voos, validar_companhia, validar_origem, validar_preco_voo
from viagem import adicionar_viagem, ver_viagens, consultar_viagem, atualizar_viagem, remover_viagem, viagens, validar_lista_nifs
from utils import validar_data, validar_telefone, validar_email, validar_NIF, validar_id, validar_id_destino, validar_id_hotel, validar_id_voo, validar_id_voo_volta, mostrar_destinos_disponiveis, mostrar_hoteis_disponiveis, mostrar_voos_disponiveis, mostrar_nifs_disponiveis, mostrar_viagens_disponiveis

def menu():
    while True:
        print("\n----------------------------- Gestor de Viagens ----------------------------")
        print("1 - Adicionar viajante     6 - Adicionar destino     11 - Adicionar hotel")
        print("2 - Ver viajantes          7 - Ver destinos          12 - Ver hoteis")
        print("3 - Consultar viajante     8 - Consultar destino     13 - Consultar hotel")
        print("4 - Atualizar viajante     9 - Atualizar destino     14 - Atualizar hotel")
        print("5 - Remover viajante       10 - Remover destino      15 - Remover hotel")
        print("")
        print("16 - Adicionar voo         21 - Adicionar viagem")
        print("17 - Ver voos              22 - Ver viagens")
        print("18 - Consultar voo         23 - Consultar viagem")
        print("19 - Atualizar voo         24 - Atualizar viagem")
        print("20 - Remover voo           25 - Remover viagem")
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
                print("\n=== CONSULTAR VIAJANTE ===")
                for chave, valor in return_code[1].items():
                    print(chave, ":", valor)
                print()
                print("Viajante listado com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "4":
            if not viajantes:
                print("Erro: Não existem utilizadores registados.")
            else:
                print("\n=== ATUALIZAR VIAJANTE ===")
                nome_procurar = input("Digite o nome do viajante para atualizar: ").strip()
                print("Digite os novos dados:")

                nome = input("Digite o novo nome:")
                nome = validar_nome(nome)

                data_nascimento = input("Digite a nova data de nascimento(DD/MM/AAAA):")
                data_nascimento = validar_data(data_nascimento)

                nacionalidade = input("Digite a nova nacionalidade:")
                nacionalidade = validar_nacionalidade(nacionalidade)

                telefone = input("Digite o novo telefone:")
                telefone = validar_telefone(telefone)

                email = input("Digite o novo email:")
                email = validar_email(email)

                NIF = input("Digite o novo NIF:")
                NIF = validar_NIF(NIF)

                interesses = input("Digite os novos interesses:")
                interesses = validar_interesses(interesses)

                orcamento = input("Digite o novo orçamento(€):")
                orcamento = validar_orcamento(orcamento)

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


        # DEPOIS

        elif opcao == "8":
            if not destinos:
                print("Erro: Não existem destinos registados.")
            else:
                mostrar_destinos_disponiveis(destinos)
                id = validar_id("Digite o ID do destino para consultar: ")
                return_code = consultar_destinos(id)
                if return_code[0] == 200:
                    print("\n=== CONSULTAR DESTINO ===")
                    for chave, valor in return_code[1].items():
                        print(chave, ":", valor)
                    print()
                    print("Destino listado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "9":
            if not destinos:
                print("Erro: Não existem destinos registados.")
            else:
                print("\n=== ATUALIZAR DESTINO ===")
                mostrar_destinos_disponiveis(destinos)
                id = validar_id("Digite o ID do destino para atualizar: ")
                print("Digite os novos dados:")

                pais = input("Digite o novo país:")
                pais = validar_pais(pais)

                cidade = input("Digite a nova cidade:")
                cidade = validar_cidade(cidade)

                tipo = input("Digite o novo tipo:")
                tipo = validar_tipo(tipo)

                atracoes = input("Digite as novas atrações:")
                atracoes = validar_atracoes(atracoes)

                return_code = atualizar_destino(id, pais, cidade, tipo, atracoes)
                if return_code[0] == 200:
                    print("Destino atualizado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "10":
            if not destinos:
                print("Erro: Não existem destinos registados.")
            else:
                mostrar_destinos_disponiveis(destinos)
                id = validar_id("Digite o ID do destino para remover: ")
                return_code = remover_destino(id)
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
            if not hoteis:
                print("Erro: Não existem hoteis registados.")
            else:
                mostrar_hoteis_disponiveis(hoteis)
                id = validar_id("Digite o ID do hotel para consultar: ")
                return_code = consultar_hotel(id)
                if return_code[0] == 200:
                    for chave, valor in return_code[1].items():
                        print(chave, ":", valor)
                    print()
                    print("Hotel listado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "14":
            if not hoteis:
                print("Erro: Não existem hoteis registados.")
            else:
                print("\n=== ATUALIZAR HOTEL ===")
                mostrar_hoteis_disponiveis(hoteis)
                id = validar_id("Digite o ID do hotel para atualizar: ")
                print("Digite os novos dados:")

                nome_hotel = input("Digite o novo nome do hotel:")
                nome_hotel = validar_hotel(nome_hotel)

                local = input("Digite a nova localizacao(cidade):")
                local = validar_local(local)

                preco = input("Digite o novo preço por noite(€):")
                preco = validar_preco(preco)

                tipo_hotel = input("Digite o novo tipo de hospedagem (hotel, pousada, resort):")
                tipo_hotel = validar_tipo_hotel(tipo_hotel)

                return_code = atualizar_hotel(id, nome_hotel, local, preco, tipo_hotel)
                if return_code[0] == 200:
                    print("Hotel atualizado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "15":
            if not hoteis:
                print("Erro: Não existem hoteis registados.")
            else:
                mostrar_hoteis_disponiveis(hoteis)
                id = validar_id("Digite o ID do hotel para remover: ")
                return_code = remover_hotel(id)
                if return_code[0] == 200:
                    print("Hotel removido com sucesso.")
                else:
                    print("Erro: " + return_code[1])

#############################################################################################

        elif opcao == "16":
            if not destinos:
                print("Erro: Não existem destinos registados.")
            else:
                print("\n=== ADICIONAR VOO ===")
                companhia = input("Digite o nome da companhia aérea:")
                companhia = validar_companhia(companhia)

                origem = input("Digite a cidade de origem:")
                origem = validar_origem(origem)

                mostrar_destinos_disponiveis(destinos)
                id_destino, erro = validar_id_destino("Digite o ID do destino: ", destinos)
                if erro:
                    print("Erro: " + erro)
                    continue

                data_partida = input("Digite a data de partida (DD/MM/AAAA):")
                data_partida = validar_data(data_partida)

                data_chegada = input("Digite a data de chegada (DD/MM/AAAA):")
                data_chegada = validar_data(data_chegada)

                preco = input("Digite o preço do voo (€):")
                preco = validar_preco_voo(preco)

                return_code = adicionar_voo(companhia, origem, id_destino, data_partida, data_chegada, preco)
                if return_code[0] == 201:
                    print("Voo adicionado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "17":
            return_code = ver_voos()
            if return_code[0] == 200:
                print("\n=== LISTA DE VOOS ===")
                for voo in return_code[1]:
                    for chave, valor in voo.items():
                        print(chave, ":", valor)
                    print()
                print("Voos listados com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "18":
            if not voos:
                print("Erro: Não existem voos registados.")
            else:
                mostrar_voos_disponiveis(voos)
                id = validar_id("Digite o ID do voo para consultar: ")
                return_code = consultar_voo(id)
                if return_code[0] == 200:
                    for chave, valor in return_code[1].items():
                        print(chave, ":", valor)
                    print()
                    print("Voo listado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "19":
            if not voos:
                print("Erro: Não existem voos registados.")
            else:
                print("\n=== ATUALIZAR VOO ===")
                mostrar_voos_disponiveis(voos)
                id = validar_id("Digite o ID do voo para atualizar: ")
                print("Digite os novos dados:")

                companhia = input("Digite a nova companhia aérea:")
                companhia = validar_companhia(companhia)

                origem = input("Digite a nova cidade de origem:")
                origem = validar_origem(origem)

                mostrar_destinos_disponiveis(destinos)
                id_destino, erro = validar_id_destino("Digite o novo ID do destino: ", destinos)
                if erro:
                    print("Erro: " + erro)
                    continue

                data_partida = input("Digite a nova data de partida (DD/MM/AAAA):")
                data_partida = validar_data(data_partida)

                data_chegada = input("Digite a nova data de chegada (DD/MM/AAAA):")
                data_chegada = validar_data(data_chegada)

                preco = input("Digite o novo preço do voo (€):")
                preco = validar_preco_voo(preco)

                return_code = atualizar_voo(id, companhia, origem, id_destino, data_partida, data_chegada, preco)
                if return_code[0] == 200:
                    print("Voo atualizado com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "20":
            if not voos:
                print("Erro: Não existem voos registados.")
            else:
                mostrar_voos_disponiveis(voos)
                id = validar_id("Digite o ID do voo para remover: ")
                return_code = remover_voo(id)
                if return_code[0] == 200:
                    print("Voo removido com sucesso.")
                else:
                    print("Erro: " + return_code[1])

#############################################################################################

        elif opcao == "21":
            if not voos:
                print("Erro: Não existem voos registados.")
            elif not hoteis:
                print("Erro: Não existem hoteis registados.")
            elif not destinos:
                print("Erro: Não existem destinos registados.")
            elif not viajantes:
                print("Erro: Não existem viajantes registados.")
            else:
                print("\n=== ADICIONAR VIAGEM ===")

                mostrar_voos_disponiveis(voos)
                id_voo_ida, erro = validar_id_voo("Digite o ID do voo de ida: ", voos)
                if erro:
                    print("Erro: " + erro)
                    continue

                id_voo_volta, erro = validar_id_voo_volta("Digite o ID do voo de volta: ", voos)
                if erro:
                    print("Erro: " + erro)
                    continue

                mostrar_nifs_disponiveis(viajantes)
                lista_nifs_str = input("Digite os NIFs dos viajantes (separados por vírgula):")
                lista_id_viajantes = validar_lista_nifs(lista_nifs_str)

                mostrar_hoteis_disponiveis(hoteis)
                id_hotel, erro = validar_id_hotel("Digite o ID do hotel: ", hoteis)
                if erro:
                    print("Erro: " + erro)
                    continue

                mostrar_destinos_disponiveis(destinos)
                id_destino, erro = validar_id_destino("Digite o ID do destino: ", destinos)
                if erro:
                    print("Erro: " + erro)
                    continue

                return_code = adicionar_viagem(id_voo_ida, id_voo_volta, lista_id_viajantes, id_hotel, id_destino)
                if return_code[0] == 201:
                    print("Viagem criada com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "22":
            return_code = ver_viagens()
            if return_code[0] == 200:
                print("\n=== LISTA DE VIAGENS ===")
                for viagem in return_code[1]:
                    for chave, valor in viagem.items():
                        print(chave, ":", valor)
                    print()
                print("Viagens listadas com sucesso.")
            else:
                print("Erro: " + return_code[1])

        elif opcao == "23":
            if not viagens:
                print("Erro: Não existem viagens registadas.")
            else:
                mostrar_viagens_disponiveis(viagens)
                id = validar_id("Digite o ID da viagem para consultar: ")
                return_code = consultar_viagem(id)
                if return_code[0] == 200:
                    for chave, valor in return_code[1].items():
                        print(chave, ":", valor)
                    print()
                    print("Viagem listada com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "24":
            if not viagens:
                print("Erro: Não existem viagens registadas.")
            else:
                print("\n=== ATUALIZAR VIAGEM ===")
                mostrar_viagens_disponiveis(viagens)
                id = validar_id("Digite o ID da viagem para atualizar: ")
                print("Digite os novos dados:")

                mostrar_voos_disponiveis(voos)
                id_voo_ida, erro = validar_id_voo("Digite o novo ID do voo de ida: ", voos)
                if erro:
                    print("Erro: " + erro)
                    continue

                id_voo_volta, erro = validar_id_voo_volta("Digite o novo ID do voo de volta: ", voos)
                if erro:
                    print("Erro: " + erro)
                    continue

                mostrar_nifs_disponiveis(viajantes)
                lista_nifs_str = input("Digite os novos NIFs dos viajantes (separados por vírgula):")
                lista_id_viajantes = validar_lista_nifs(lista_nifs_str)

                mostrar_hoteis_disponiveis(hoteis)
                id_hotel, erro = validar_id_hotel("Digite o novo ID do hotel: ", hoteis)
                if erro:
                    print("Erro: " + erro)
                    continue

                mostrar_destinos_disponiveis(destinos)
                id_destino, erro = validar_id_destino("Digite o novo ID do destino: ", destinos)
                if erro:
                    print("Erro: " + erro)
                    continue

                return_code = atualizar_viagem(id, id_voo_ida, id_voo_volta, lista_id_viajantes, id_hotel, id_destino)
                if return_code[0] == 200:
                    print("Viagem atualizada com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "25":
            if not viagens:
                print("Erro: Não existem viagens registadas.")
            else:
                mostrar_viagens_disponiveis(viagens)
                id = validar_id("Digite o ID da viagem para remover: ")
                return_code = remover_viagem(id)
                if return_code[0] == 200:
                    print("Viagem removida com sucesso.")
                else:
                    print("Erro: " + return_code[1])

        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == '__main__':
    menu()
