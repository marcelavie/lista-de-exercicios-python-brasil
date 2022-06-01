"""
Exercício 18 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Arredonde o tempo em minutos

    >>> from secao_01_estrutura_sequencial import ex_18_tempo_de_download
    >>> numeros =['50', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 7 minuto(s)
    >>> numeros =['100', '2500']
    >>> ex_18_tempo_de_download.input = lambda k: numeros.pop()
    >>> ex_18_tempo_de_download.calcular_tempo_de_download()
    O tempo aproximado do Download é: 3 minuto(s)

"""


def calcular_tempo_de_download():
    """Escreva aqui em baixo a sua solução"""
    tamanho = int(input('Qual é o tamanho do arquivo (em MB)? '))
    velocidade = int(input('Qual a velocidade do link em Mbps? '))
    tamanho_em_bits= tamanho*8
    tempo_segundos= tamanho_em_bits/velocidade
    tempo_minutos= tempo_segundos/60
    print(f'O tempo aproximado do Download é: {tempo_minutos:.0f} minuto(s)')