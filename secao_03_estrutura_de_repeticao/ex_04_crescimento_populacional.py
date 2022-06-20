"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

    >>> calcular_ano_ultrapassagem_populacional()
    'População de A, depois de 63 ano(s) será de 515033 pessoas, superando a de B, que será de 510964 pessoas'


"""


def calcular_ano_ultrapassagem_populacional() -> str:
    """Escreva aqui em baixo a sua solução"""

    populacao_a = 80000
    taxa_crescimento_a = 3
    taxa_crescimento_a_em_porcentagem = taxa_crescimento_a/100
    populacao_b = 200000
    taxa_crescimento_b = 1.5
    taxa_Crescimento_b_em_porcentagem = taxa_crescimento_b/100
    anos = 0
    while populacao_a < populacao_b:
        populacao_a = populacao_a + (populacao_a*taxa_crescimento_a_em_porcentagem)
        populacao_b = populacao_b + (populacao_b*taxa_Crescimento_b_em_porcentagem)
        anos += 1
    
    return 'População de A, depois de %i ano(s) será de %i pessoas, superando a de B, que será de %i pessoas'%(anos,populacao_a,populacao_b)
