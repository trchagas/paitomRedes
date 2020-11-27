def salva_estado(lst_dispositivo):
    linhas = leitura_estado()
    matriz = []
    for linha in linhas:
        matriz.append(linha.split("#"))
    f = open("estado.txt", "a")
    flag = True
    for dispositivo in lst_dispositivo:
        for linha in matriz:
            if(dispositivo[1] == linha[1]):
                flag = False
        if flag:
            f.write(dispositivo[0] + "#" + dispositivo[1] + "#" + dispositivo[2] + "#" + dispositivo[3] + "#" + dispositivo[4] + "#" + dispositivo[5] + "\n")
        flag = True

def leitura_estado():
    with open("estado.txt", "rt") as fr:
        return fr.readlines()

def print_definido(indice, item):
    if (item == "\n"):
        return
    if (indice == 0):
        print(f"Tipo: {item}")
    elif (indice == 1):
        print(f"IP: {item}")
    elif (indice == 2):
        print(f"Mac: {item}")
    elif (indice == 3):
        print(f"Fabricante: {item}")
    elif (indice == 4):
        print(f"Status: {item}")
    elif (indice == 5):
        print(f"Hora de Descoberta: {item}")


def mostra_estado():
    linhas = leitura_estado()
    matriz = []
    for linha in linhas:
        matriz.append(linha.split("#"))
    for linha in matriz:
        for i in range(len(linha)):
            print_definido(i, linha[i])

def todos_offline():
    linhas = leitura_estado()
    with open("estado.txt", "wt") as fw:
        for linha in linhas:
            fw.write(linha.replace("Online", "Offline"))

def definir_dispositivo_online(ip):
    linhas = leitura_estado()
    dispositivos = []
    for linha in linhas:
        vet = linha.strip()
        dispositivos.append(vet.split("#"))
    novas_linhas = ""
    for i in range(len(dispositivos)):
        if dispositivos[i][1] == ip:
            linhas[i] = linhas[i].replace("Offline", "Online")
        novas_linhas += linhas[i]
    with open("estado.txt", "wt") as fw:
                fw.write(novas_linhas)

def descobre_tipo(lst_dispositivo):
    maior = 0
    menor = 255

    for dispositivo in lst_dispositivo:
        ip_lst = (dispositivo[1].split("."))
        ip_ultimo_num = int(ip_lst[len(ip_lst)-1])
        if ip_ultimo_num > maior:
            maior = ip_ultimo_num
        if ip_ultimo_num < menor:
            menor = ip_ultimo_num

    for dispositivo in lst_dispositivo:
        ip_lst = (dispositivo[1].split("."))
        ip_ultimo_num = int(ip_lst[len(ip_lst) - 1])
        if ip_ultimo_num is maior or ip_ultimo_num is menor:
            dispositivo[0] = "Roteador"
        else:
            dispositivo[0] = "Host"
