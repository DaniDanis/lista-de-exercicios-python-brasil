"""
Exercício 27 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
de alunos para cada turma. As turmas não podem ter mais de 40 alunos e devem ter ao menos um aluno.
Arredonde o valor da média para baixo.

    >>> from secao_03_estrutura_de_repeticao import ex_27_alunos_por_turma
    >>> entradas = ['1', '1']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 1
    Média de alunos por turma: 1
    >>> entradas = ['40', '40', '2']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 2
    Média de alunos por turma: 40
    >>> entradas = ['10', '20', '30', '40', '-1', '4']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 4
    Uma turma deve ter de 1 a 40 alunos, não é possível ter -1 alunos
    Média de alunos por turma: 25
    >>> entradas = ['10', '20', '30', '0', '41', '3']
    >>> ex_27_alunos_por_turma.input = lambda k: entradas.pop()
    >>> ex_27_alunos_por_turma.calcular_media_de_alunos_por_turma()
    Número de turmas: 3
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 41 alunos
    Uma turma deve ter de 1 a 40 alunos, não é possível ter 0 alunos
    Média de alunos por turma: 20

"""


def calcular_media_de_alunos_por_turma():
    """Escreva aqui em baixo a sua solução"""    
    entradas = []
    entradas.append(int(input('Insira o número de turmas: ')))
    contador = 0
    soma_alunos = 0
    turma = entradas[0]
    turma_teste = 0
    print('Número de turmas: %.0f'% turma)
    while contador < len(entradas):
        entradas.insert(0, int(input('Insira a quantidade de alunos: ')))
        contador = contador + 1
        if entradas[0] <= 0 or entradas[0] > 40:
            print('Uma turma deve ter de 1 a 40 alunos, não é possível ter %.0f alunos'%entradas[0])
        else:            
            soma_alunos = soma_alunos + entradas[0]     
            turma_teste = turma_teste + 1
        if turma_teste == turma:
            media = soma_alunos/entradas[len(entradas)-1]            
            contador = contador + 1
    else:
        print('Média de alunos por turma: %.0f'% media)
    
            

