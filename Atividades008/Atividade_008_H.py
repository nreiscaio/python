# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data início: 29/11/2021
# Término: 29/11/2021
# Exercício H

#Importando biblioteca: 
import os

#Limpando terminal:
os.system('cls')

#Título: 
print('-'*50)
print('Programa que lê um número indeterminado de notas')
print('='*50)

#Declarações:
listaNotas = []
soma = 0
media = 0
quantidade = 0

while (True):
    print('='*50)

    #Entrada de dados:
    nota = input('Digite a nota [s ou 0 sair]: ').lower()
    
    if(nota == 's' or '0'):               
        break
    
    #Validação:
    else:
        if ((not(nota.isnumeric()))):
            print()
            print(f'Entrada Inválida, digite novamente...')
            print()
        else:
             nota = float(nota)
             listaNotas.append(nota)
             soma += nota
             quantidade += 1
             media = soma / quantidade

#Funções de listas:
quantidadeNotas = len(listaNotas)
listaInversa = sorted(listaNotas, reverse=True)

#Saída:
print()
print('='*50)
print(f'A quantidade de notas lidas foi: {quantidadeNotas}')
print(f'As notas na ordem informada são: {listaNotas}')
print(f'As notas na ordem iversa são: {listaInversa}')
print(f'A soma das notas é: {soma}')
print(f'A média das notas é: {media:.2f}')
print()
print('-'*50)
print('Fim do programa!')
print('='*50)