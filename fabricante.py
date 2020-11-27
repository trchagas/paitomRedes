import requests

def get_mac_details(mac_address):
    url = "https://api.macvendors.com/"

    response = requests.get(url + mac_address)
    if response.status_code != 200:
        raise Exception("IP MAC nao encontrado!")
    return response.content.decode()