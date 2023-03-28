import cotacoes
'''
Proximos passos:  
Perguntar qual é a moeda inicial / final
Adicionar mais moedas 

'''
while True:
    print("***********************")
    print(" CONVERSOR DE MOEDAS ")
    print("***********************")

    option = int(input('Informe a moeda para qual deseja efetuar a conversão:\n'
                       '1 - Dolar\n'
                       '2 - Euro\n'
                       '3 - Iene\n'))

    # msg = f'R$ {valor:.2f} em USD é ${resultado:.2f}'
    if option == 1:
        valor = float(input('Informe o valor em real: '))
        cotacao = cotacoes.cotacao_dolar()
        resultado = valor / cotacao
        msg = f'R$ {valor:.2f} em USD é ${resultado:.2f}'
        print(msg)
    elif option == 2:
        valor = float(input('Informe o valor em real: '))
        cotacao = cotacoes.cotacao_euro()
        resultado = valor / cotacao
        msg = f'R$ {valor:.2f} em EUR é €{resultado:.2f}'
        print(msg)
    elif option == 3:
        valor = float(input('Informe o valor em real: '))
        cotacao = cotacoes.cotacao_iene()
        resultado = valor / cotacao
        msg = f'R$ {valor:.2f} em JPY é ¥{resultado:.2f}'
        print(msg)
    if option not in [1, 2, 3]:
        print('Opção invalida! Tente novamente!')
