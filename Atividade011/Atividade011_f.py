# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data início: 07/02/2022
# Término: 07/02/2022

import os
os.system('cls')


def cadastrar():
    pessoa = {}
    listaPessoas = []

    for c in range(2):
        
        pessoa['Nome'] = str(input(f'{c+1}ª.Nome: '))
        pessoa['Peso'] = float(input(f'{c+1}ª.Peso: '))
        pessoa['Idade'] = str(input(f'{c+1}ª.Idade: '))

        listaPessoas.append(pessoa.copy())



    os.system('cls')
    print('-'*50)
    print('Alunos Cadastrados')
    print('='*50)

    for aluno in listaPessoas:
        for chave, valor in aluno.items():
            print(f'{chave}  {valor}', end=' ' + '\n')
        print('-'*50)

    


#Programa Principal:
print('-'*50)
print('Cadastro de Alunos')
print('='*50)
cadastrar()
