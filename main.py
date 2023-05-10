import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


moedas = {
    "Dolar": "USD",
    "Euro": "EUR",
    "Iene": "JPY",
    "Libra Esterlina": "GBP",
    "Franco Suiço": "CHF",
    "Bitcoin" : "BTC"
}

def obter_cotacao(moeda):
    response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}")
    if response.status_code == 200:
        data = response.json()
        high = float(data[f"{moeda}BRL"]["high"])
        return high
    return None

def converter_moeda():
    valor = float(valor_entry.get())
    moeda_origem = moeda_origem_combobox.get()
    moeda_destino = moeda_destino_combobox.get()
    
    cotacao_origem = obter_cotacao(moedas[moeda_origem])
    cotacao_destino = obter_cotacao(moedas[moeda_destino])
    
    if cotacao_origem is not None and cotacao_destino is not None:
        result = valor * cotacao_origem / cotacao_destino
        msg = f'${valor:.2f} em {moeda_origem} é {result:.2f} em {moeda_destino}'
        messagebox.showinfo("Resultado", msg)
    else:
        messagebox.showerror("Erro", "Não foi possível obter as informações de cotação")
        


root = tk.Tk()
root.title('Conversor de moedas')


rotulo = tk.Label(root, text='Valor em real')
rotulo.pack

valor_entry = tk.Entry(root)
valor_entry.pack()

rotulo_origem = tk.Label(root, text='Moeda de origem')
rotulo_origem.pack()

moeda_origem_combobox = ttk.Combobox(root, values=list(moedas.keys()))
moeda_origem_combobox.pack()


rotulo_destino = tk.Label(root, text='Moeda de destino')
rotulo_destino.pack()

moeda_destino_combobox = ttk.Combobox(root, values=list(moedas.keys()))
moeda_destino_combobox.pack()

botao = tk.Button(root, text='Converter', command=converter_moeda)
botao.pack()

root.mainloop()