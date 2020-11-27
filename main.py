from pathlib import Path

from historico import *
from descoberta import *
from dispositivos import *

if __name__ == "__main__":
    Path("estado.txt").touch()
    Path("historico.txt").touch()

    lst_dispositivo = []

    while True:
        print("Menu:\n")
        print("1 - Buscar Dispositivos e Mostrar Estado Atual")
        print("2 - Mostrar Historico\n")

        opcao = int(input("Input: "))
        if(opcao == 1):
            print("Buscando...\n")
            lst_ip = map_network()
            lst_dispositivo = gera_lista(lst_ip)
            salva_estado(lst_dispositivo)
            salva_estado_historico()
            todos_offline()
            for ip in lst_ip:
                definir_dispositivo_online(ip)
            mostra_estado()
        elif(opcao == 2):
            mostra_historico()
        else:
            print("Input Invalido")

        input("\n Pressione Enter para continuar...")
        print('\n' * 80)







