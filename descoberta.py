import socket
import multiprocessing
import subprocess
import os

def pinger(fila_trab, fila_resultados):
    DEVNULL = open(os.devnull, 'w')
    while True:
        ip = fila_trab.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip], stdout=DEVNULL)
            fila_resultados.put(ip)
        except:
            pass


def busca_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


def map_network(tam_pool=255):
    lst_ip = list()

    ip_partes = busca_ip().split('.')
    ip_base = ip_partes[0] + '.' + ip_partes[1] + '.' + ip_partes[2] + '.'

    trabs = multiprocessing.Queue()
    resultados = multiprocessing.Queue()

    pool = [multiprocessing.Process(target=pinger, args=(trabs, resultados)) for i in range(tam_pool)]

    for p in pool:
        p.start()

    for i in range(1, 255):
        trabs.put(ip_base + '{0}'.format(i))

    for p in pool:
        trabs.put(None)

    for p in pool:
        p.join()

    while not resultados.empty():
        ip = resultados.get()
        lst_ip.append(ip)

    return lst_ip