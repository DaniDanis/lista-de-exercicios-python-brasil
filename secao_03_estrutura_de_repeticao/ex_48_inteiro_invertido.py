"""
Exercício 48 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaDeRepeticao

Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  entrada => 12376489
  saida => 98467321

    >>> inverter_inteiro(0)
    0
    >>> inverter_inteiro(123456789)
    987654321
    >>> inverter_inteiro(3454232311243232979128123)
    3218219792323421132324543
    >>> inverter_inteiro(987654321)
    123456789

"""


def inverter_inteiro(numero):
    """Escreva aqui em baixo a sua solução"""

    contador = 0
    invertido = []
    numero_s = str(numero)
    while len(numero_s) > contador:
      invertido.insert(0,numero_s[contador])      
      contador += 1
      if contador == len(numero_s):
        contador = 0
        while len(invertido) > contador:
          print(invertido[contador],end='')
          contador += 1
