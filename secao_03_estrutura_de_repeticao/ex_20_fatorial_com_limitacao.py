"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120

Limite o cáculo para valores inteiros, positivos, maiores ou iguais a 16.

    >>> calcular_fatorial(1)
    1
    >>> calcular_fatorial(2)
    2
    >>> calcular_fatorial(3)
    6
    >>> calcular_fatorial(4)
    24
    >>> calcular_fatorial(5)
    120
    >>> calcular_fatorial(16)
    20922789888000
    >>> calcular_fatorial(17)
    'Apenas valores positivos, inteiros e menores que 16 são válidos. Não é possível calcular para 17'
    >>> calcular_fatorial(0)
    'Apenas valores positivos, inteiros e menores que 16 são válidos. Não é possível calcular para 0'
    >>> calcular_fatorial(-1)
    'Apenas valores positivos, inteiros e menores que 16 são válidos. Não é possível calcular para -1'
    >>> calcular_fatorial(3.14)
    'Apenas valores positivos, inteiros e menores que 16 são válidos. Não é possível calcular para 3.14'

"""


def calcular_fatorial(n: int) -> int:
    """Escreva aqui em baixo a sua solução"""

    fatorial = []
    aux = n
    calculo = 1    
    while True:
        if n <= 0 or n > 16:
            print('\'Apenas valores positivos, inteiros e menores que 16 são válidos. Não é possível calcular para %.0f\''%n)
            break
        if int(str(float(n)).split(('.'))[1]) >= 1:
            print('\'Apenas valores positivos, inteiros e menores que 16 são válidos. Não é possível calcular para %.2f\''%n)
            break
        else:
            fatorial.append(n)        
            n = n-1
            if aux == 0 or aux == 1:
                print(1)
                break
            if n >= 0:              
                calculo = fatorial[len(fatorial)-1]*calculo                    
                if n == 0:
                    print(calculo) 
                    break
        