"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o custo seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

    >>> from secao_01_estrutura_sequencial import ex_17_loja_de_tintas_complexa
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '100'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 19 litros de tinta.
    Você pode comprar 2 lata(s) de 18 litros a um custo de R$ 160. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 6 lata(s) de 3.6 litros a um custo de R$ 150. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 1 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 105. Vão sobrar 2.6 litro(s) de tinta.
    >>> ex_17_loja_de_tintas_complexa.input = lambda k: '200'
    >>> ex_17_loja_de_tintas_complexa.calcular_latas_e_preco_de_tinta()
    Você deve comprar 37 litros de tinta.
    Você pode comprar 3 lata(s) de 18 litros a um custo de R$ 240. Vão sobrar 17.0 litro(s) de tinta.
    Você pode comprar 11 lata(s) de 3.6 litros a um custo de R$ 275. Vão sobrar 2.6 litro(s) de tinta.
    Para menor custo, você pode comprar 2 lata(s) de 18 litros e 1 galão(ões) de 3.6 litros a um custo de R$ 185. Vão sobrar 2.6 litro(s) de tinta.

"""


from math import ceil


def calcular_latas_e_preco_de_tinta():
    """Escreva aqui em baixo a sua solução"""
    area_pintada = float(input('Insira o tamanho da área a ser pintada em metros quadrados'))
    litros_necessarios = ceil((area_pintada/6)+((area_pintada/6)*0.1))
    #LATAO GRANDE#
    latas_necessarias_18 = ceil(litros_necessarios/18)
    sobra_grande = (latas_necessarias_18*18)-litros_necessarios
    custo_grande = latas_necessarias_18*80
    #LATAO PEQUENO#
    latas_necessarias_3 = ceil(litros_necessarios/3.6)    
    custo_pequena = latas_necessarias_3*25
    sobra_pequena = (latas_necessarias_3*3.6)-litros_necessarios
    #CONTA ECONOMICA#
    latas_necessaria_18_economica = latas_necessarias_18 - 1
    latas_necessaria_3_economica = ceil((litros_necessarios-(18*latas_necessaria_18_economica))/3.6)
    custo_economica = (latas_necessaria_18_economica*80)+(latas_necessaria_3_economica*25) 
    sobra_economica = ((latas_necessaria_18_economica*18)+(latas_necessaria_3_economica*3.6)-litros_necessarios)     
    print('Você deve comprar', litros_necessarios, 'litros de tinta.')
    print('Você pode comprar', latas_necessarias_18, 'lata(s) de 18 litros a um custo de R$', '%.0f.' %custo_grande, 'Vão sobrar', '%.1f' %sobra_grande,'litro(s) de tinta.')
    print('Você pode comprar', latas_necessarias_3, 'lata(s) de 3.6 litros a um custo de R$', '%.0f.' %custo_pequena, 'Vão sobrar', '%.1f' %sobra_pequena,'litro(s) de tinta.')
    if sobra_grande > 10.8:
        print('Para menor custo, você pode comprar', latas_necessaria_18_economica, 'lata(s) de 18 litros e', latas_necessaria_3_economica, 'galão(ões) de 3.6 litros a um custo de R$', '%.0f.'% custo_economica, 'Vão sobrar %.1f' % sobra_economica, 'litro(s) de tinta.')
    else:
        print('Para menor custo, você pode comprar', latas_necessarias_18, 'lata(s) de 18 litros e nenhum galão(ões) de 3.6 litros a um custo de R$', '%.0f.'% custo_grande, 'Vão sobrar %.1f' % sobra_grande, 'litro(s) de tinta.')
        
