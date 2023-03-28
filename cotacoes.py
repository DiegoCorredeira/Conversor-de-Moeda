import requests

euro = 'EUR'
dolar = 'USD'
iene = 'JPY'
def cotacao_dolar():
    response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{dolar}")
    if response.status_code == 200:
        data = response.json()
        high =  float(data['USDBRL']['high'])
        return high

def cotacao_euro():
        response = requests.get(f'https://economia.awesomeapi.com.br/json/last/{euro}')
        if response.status_code == 200:
            data = response.json()
            high =  float(data['EURBRL']['high'])
            return high
cotacao_euro()

def cotacao_iene():
        response = requests.get(f'https://economia.awesomeapi.com.br/json/last/{iene}')
        if response.status_code == 200:
            data = response.json()
            high =  float(data['JPYBRL']['high'])
            return high


