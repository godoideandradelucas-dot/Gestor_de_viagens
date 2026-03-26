from viajantes import adicionar_viajante, ver_viajantes, consultar_viajantes, atualizar_viajantes, remover_viajantes
from destino import adicionar_destino, ver_destinos, consultar_destinos, atualizar_destino, remover_destino
from hotel import adicionar_hotel, ver_hoteis, consultar_hotel, atualizar_hotel, remover_hotel

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
            adicionar_viajante()
        elif opcao == "2":
            ver_viajantes()
        elif opcao == "3":
            consultar_viajantes()
        elif opcao == "4":
            atualizar_viajantes()
        elif opcao == "5":
            remover_viajantes()
        elif opcao == "6":
            adicionar_destino()
        elif opcao == "7":
            ver_destinos()
        elif opcao == "8":
            consultar_destinos()
        elif opcao == "9":
            atualizar_destino()
        elif opcao == "10":
            remover_destino()
        elif opcao == "11":
            adicionar_hotel()
        elif opcao == "12":
            ver_hoteis()
        elif opcao == "13":
            consultar_hotel()
        elif opcao == "14":
            atualizar_hotel()
        elif opcao == "15":
            remover_hotel()
        elif opcao == "0":
            print("saindo do sistema...")
            break
        else:
            print("opção invalida!")


if __name__ == '__main__':
    menu()