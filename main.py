from netdisco.discovery import NetworkDiscovery
from getmac import get_mac_address
import datetime

netdis = NetworkDiscovery()

netdis.scan()

now = datetime.datetime.now()

for dev in netdis.discover():
    host = netdis.get_info(dev)[0]["host"]
    fabricante = netdis.get_info(dev)[0]["manufacturer"]
    ip_mac = get_mac_address(ip=host)
    #Mudar print para adicionar a uma lista, pra pode armazenar dps
    #A hora não pode atualizar depois da primeira vez
    print(f"IP: {host} - IP-MAC {ip_mac} - Fabricante: {fabricante} - Hora de descoberta: {now.hour}:{now.minute}:{now.second}".format(host = host, manufacturer = fabricante))
    print("\n")

netdis.stop()