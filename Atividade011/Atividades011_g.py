# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data de Início: 07/02/2022
# Término: 07/02/2022

# Importando as bibliotecas:
import os

# Limpando o terminal:
os.system('cls')


def soma():
    """[Função que soma valores]

    Args:
        a ([float]): [Valor de a]
        b ([float]): [Valor de b]

    Returns:
        [input]: [Soma dos valores a e b]
    """
    a = float(input('Digite o numero "a": '))
    b = float(input('Digite o numero "b": '))

    soma = a + b
    print(soma)


def subtracao():
    """[Função que subtrai valores]

    Args:
        a ([int]): [Valor de a]
        b ([int]): [Valor de b]

    Returns:
        [input]: [Subtração dos valores a e b]
    """
    a = float(input('Digite o numero "a": '))
    b = float(input('Digite o numero "b": '))
    subtracao = a - b

    print(subtracao)


def multiplicacao():
    """[Função que multiplica valores]

    Args:
        a ([int]): [Valor de a]
        b ([int]): [Valor de b]

    Returns:
        [input]: [Multiplicação dos valores a e b]
    """
    a = float(input('Digite o numero "a": '))
    b = float(input('Digite o numero "b": '))
    multiplicacao = a * b

    print(multiplicacao)


def divisao():
    """[Função que multiplica valores]

    Args:
        a ([float]): [Valor de a]
        b ([float]): [Valor de b]

    Returns:
        [input]: [Divisão dos valores a e b]
    """
    a = float(input('Digite o numero "a": '))
    b = float(input('Digite o numero "b": '))
    divisao = a * b

    print(divisao)


def divisao_inteiro():
    """[Função que multiplica valores]

    Args:
        a ([float]): [Valor de a]
        b ([float]): [Valor de b]

    Returns:
        [input]: [Divisão inteira dos valores a e b]
    """
    a = float(input('Digite o numero "a": '))
    b = float(input('Digite o numero "b": '))
    divisao_inteiro = a // b

    print(divisao_inteiro)


def resto_divisao():
    """[Função que multiplica valores]

    Args:
        a ([float]): [Valor de a]
        b ([float]): [Valor de b]

    Returns:
        [input]: [Resto divisão dos valores a e b]
    """
    a = float(input('Digite o numero "a": '))
    b = float(input('Digite o numero "b": '))
    resto_divisao = a % b

    print(resto_divisao)


print('-'*50)
print('Calculadora')
print('='*50)
print()
print('Digite "1" para soma; "2" para subtração; "3" para multiplicação;')
print('"4" para divisão; "5" para divisão de inteiro;')
print('"6" para resto de divisão; "7" para saída')
print('-'*50)
print()
digito = str(input('Digite o codigo: '))


if digito == '1':
    soma()
    print('Você finalizou o programa!')

elif digito == '2':
    subtracao()
    print('Você finalizou o programa!')

elif digito == '3':
    multiplicacao()
    print('Você finalizou o programa!')

elif digito == '4':
    divisao()
    print('Você finalizou o programa!')

elif digito == '5':
    divisao_inteiro()
    print('Você finalizou o programa!')

elif digito == '6':
    resto_divisao()
    print('Você finalizou o programa!')

else:
    digito == 's'
    print('Você encerrou o programa!')
    exit
