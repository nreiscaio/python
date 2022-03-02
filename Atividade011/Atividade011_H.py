# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data de Início: 07/02/2022
# Término: 07/02/2022

# Importando as bibliotecas:
import os

# Limpando o terminal:
os.system('cls')


def cadastrar():
    pessoa = {}
    listaPessoas = []

    for c in range(1):

        pessoa['Código pessoa 1'] = str(input('Nome pessoa 1: '))
        pessoa['Código pessoa 2'] = str(input('Nome pessoa 2: '))
        pessoa['Código pessoa 3'] = str(input('Nome pessoa 3: '))

        listaPessoas.append(pessoa.copy())



    return listaPessoas


def cadastro2():
    dadosPessoa = {}
    listaPessoa = []

    for c in range(3):

        dadosPessoa['Altura'] = float(input('Altura pessoa 1: '))
        dadosPessoa['Altura'] = float(input('Altura pessoa 2: '))
        dadosPessoa['Altura'] = float(input('Altura pessoa 3: '))

        valores = dadosPessoa.values()

        return valores


def cadastro3():
    dadosPessoal = {}
    listaPessoal = []

    for c in range(3):

        dadosPessoal['Peso'] = float(input('Peso pessoa 1: '))
        dadosPessoal['Peso'] = float(input('Peso pessoa 2: '))
        dadosPessoal['Peso'] = float(input('Peso pessoa 3: '))

        valores2 = dadosPessoal.values()

        return valores2


# Programa Principal:
print('-'*50)
print('Cadastro de Alunos')
print('='*50)
listas = cadastrar()
lista = cadastro2()
lista2 = cadastro3()

print(listas, lista, lista2)
