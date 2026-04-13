from destino import adicionar_destino, ver_destinos, consultar_destinos, atualizar_destino, remover_destino
from hotel import adicionar_hotel, ver_hoteis, consultar_hotel, atualizar_hotel, remover_hotel
from viajantes import adicionar_viajante, ver_viajantes, consultar_viajantes, atualizar_viajantes, remover_viajantes

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
            return_code = adicionar_viajante()
            if return_code[0] == 201:
                print("Utilizador criado com sucesso.")

        elif opcao == "2":
            return_code = ver_viajantes()
            if return_code[0] == 200:
                print("Utilizadores listados com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "3":
            return_code = consultar_viajantes()
            if return_code[0] == 200:
                print("Utilizador listado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])


        elif opcao == "4":
            return_code = atualizar_viajantes()
            if return_code[0] == 200:
                print("Utilizador atualizado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "5":
            return_code = remover_viajantes()
            if return_code[0] == 200:
                print("Utilizador removido com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "6":
            return_code = adicionar_destino()
            if return_code[0] == 201:
                print("Destino criado com sucesso.")

        elif opcao == "7":
            return_code = ver_destinos()
            if return_code[0] == 200:
                print("Destinos listados com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "8":
            return_code = consultar_destinos()
            if return_code[0] == 200:
                print("Destino listado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "9":
            return_code = atualizar_destino()
            if return_code[0] == 200:
                print("Destino atualizado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "10":
            return_code = remover_destino()
            if return_code[0] == 200:
                print("Destino removido com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "11":
            return_code = adicionar_hotel()
            if return_code[0] == 201:
                print("Hotel criado com sucesso.")

        elif opcao == "12":
            return_code = ver_hoteis()
            if return_code[0] == 200:
                print("Hoteis listados com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "13":
            return_code = consultar_hotel()
            if return_code[0] == 200:
                print("Hotel listado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "14":
            return_code = atualizar_hotel()
            if return_code[0] == 200:
                print("Hotel atualizado com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "15":
            return_code = remover_hotel()
            if return_code[0] == 200:
                print("Hotel removido com sucesso.")
            else:
                print("Internal Error: " + return_code[1])

        elif opcao == "0":
            print("saindo do sistema...")
            break
        else:
            print("opção invalida!")


if __name__ == '__main__':
    menu()