"""
Exercício 45 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno
a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma com uma casa decimal.

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

    >>> corrigir(('Renzo','A','B','C','D','E','E','D','C','B','A' ))
    Aluno                 Nota
    Renzo                 10
    ---------------------------
    Média geral: 10.0
    Maior nota: 10
    Menor nota: 10
    Total de Alunos: 1
    >>> corrigir(
    ... ('Renzo','A','B','C','D','E','E','D','C','B','A' ),
    ... ('Fulano','A','B','C','D','E','E','D','C','B','B' ),
    ... )
    Aluno                 Nota
    Renzo                 10
    Fulano                 9
    ---------------------------
    Média geral: 9.5
    Maior nota: 10
    Menor nota: 9
    Total de Alunos: 2
"""


def corrigir(*provas):
    """Escreva aqui em baixo a sua solução"""
    print('Aluno                 Nota')
    gabarito = ['Gabarito', 'A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
    soma = 0
    n = 0
    name = []
    notas = []  
    
    for (nome, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10) in provas:
        name.append(nome)

        if a1 == gabarito[n+1]:
            soma += 1
        if a2 == gabarito[n+2]:
            soma += 1
        if a3 == gabarito[n+3]:
            soma += 1
        if a4 == gabarito[n+4]:
            soma += 1
        if a5 == gabarito[n+5]:
            soma += 1
        if a6 == gabarito[n+6]:
            soma += 1
        if a7 == gabarito[n+7]:
            soma += 1
        if a8 == gabarito[n+8]:
            soma += 1
        if a9 == gabarito[n+9]:
            soma += 1
        if a10 == gabarito[n+10]:
            soma += 1
        print(f'{nome}                 {soma}')
        notas.append(soma)
        soma = 0
        media = sum(notas)/len(provas)

    print(f'---------------------------')
    print(f'Média geral: {media:.1f}')
    print(f'Maior nota: {max(notas)}')
    print(f'Menor nota: {min(notas)}')
    print(f'Total de Alunos: {len(provas)}')

