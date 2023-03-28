# Conversor de Moeda Real

###### O código Conversor de Moeda é uma aplicação simples em Python que permite ao usuário converter um valor monetário em Real para outras moedas, como Dólar, Euro e Iene.

## Bibliotecas
### O código usa as seguintes bibliotecas:

    requests: é usada para fazer solicitações HTTP para uma API de terceiros.

## Funções
### O código tem as seguintes funções:

    cotacao_dolar(): Esta função usa a API AwesomeAPI para obter a cotação do Dólar em relação ao Real. A função retorna o valor da cotação do Dólar em float.

    cotacao_euro(): Esta função usa a API AwesomeAPI para obter a cotação do Euro em relação ao Real. A função retorna o valor da cotação do Euro em float.

    cotacao_iene(): Esta função usa a API AwesomeAPI para obter a cotação do Iene em relação ao Real. A função retorna o valor da cotação do Iene em float.
## Executando o código

Para executar o código, abra o terminal ou prompt de comando, navegue até o diretório onde o arquivo do código está salvo e execute o seguinte comando: python main.py.

O usuário será solicitado a selecionar a moeda de conversão e inserir o valor monetário em Reais que deseja converter.

## Limitações

Este código tem as seguintes limitações:

    O código usa uma única API para obter as cotações das moedas. Se essa API falhar ou estiver inacessível, o código não poderá fornecer conversões precisas ou completas.
    O código só permite a conversão de Reais para Dólar, Euro e Iene. Não é possível converter outras moedas com este código.

## Futuro da aplicação

    - Adicionar mais moedas de conversão.
    - Permitir que o usuário selecione a moeda inicial e de destino.
    - Implementar uma API de backup para fornecer cotações de moedas em caso de falha na API principal.

