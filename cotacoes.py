import requests

peso_ars =  21653
dolar_usd = 10813
euro_eur = 21619

def cotacao_dolar():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{dolar_usd}/dados/ultimos/1?formato=json"
    response = requests.get(url)
    cotacao = response.json()[0]['valor']
    arredondamento_cotacao = round(float(cotacao), 2)
    return arredondamento_cotacao


def cotacao_euro():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{euro_eur}/dados/ultimos/1?formato=json"
    response = requests.get(url)
    cotacao = response.json()[0]['valor']
    arredondamento_cotacao = round(float(cotacao),2)
    return arredondamento_cotacao