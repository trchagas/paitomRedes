import datetime
from getmac import get_mac_address

from fabricante import *
from estado import *

def gera_lista(lst_ip):
    now = datetime.datetime.now()
    lst_dispositivo = []
    for ip in lst_ip:
        dispositivo = []
        tipo = " "
        try:
            mac = get_mac_address(ip=ip)
            fabricante = get_mac_details(mac)
        except:
            mac = "Nao Encontrado"
            fabricante = "Nao Encontrado"
        status = "Online"
        hora_inicial = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        dispositivo.extend([tipo, ip, mac, fabricante, status, hora_inicial])
        lst_dispositivo.append(dispositivo)

    descobre_tipo(lst_dispositivo)
    return lst_dispositivo