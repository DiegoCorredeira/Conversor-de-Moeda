import cotacoes
while True:
    print("***********************")
    print(" CONVERSOR DE MOEDAS ")
    print("***********************")

    option = int(input('Informe a moeda para qual deseja efetuar a conversão:\n'
                       '1 - Dolar\n'
                       '2 - Euro\n'))
    if option == 1:
        valor = int(input('Informe o valor em real:'))
        cotacao = cotacoes.cotacao_dolar()
        resultado = valor / cotacao
        print(f'R$ {valor:.2f} em USD é ${resultado:.2f}')
        break
    if option == 2:
        valor = int(input('Informe o valor em real: '))
        cotacao = cotacoes.cotacao_euro()
        resultado = valor / cotacao
        print(f'R$ {valor:.2f} em EUR é €{resultado:.2f}')
        break
