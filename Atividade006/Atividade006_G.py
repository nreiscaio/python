#Curso Técnico de Informática
#Autor: Caio Nascimento
#Data de início: 12/11/2021
#Término: 16/10/2021
#Atividade G

#Importando as bibliotecas:
import os

#Limpando o terminal
os.system('cls')

#Título:
print('-'*50)
print('PROGRAMA QUE RECEBE UM NUMÉRO MILHAR E MOSTE NA TELA:')
print('-QUANTIDADE DE UNIDADES')
print('-QUANTIDADE DE DEZENAS')
print('-QUANTIDADE DE CENTENAS')
print('-QUANTIDADE DE MILHAR')
print('='*50)

#Entrada de dados: 
numero = int(input('Digite um número milhar: '))

#Declaração:
unidade  = numero[3:3]
dezena = numero[2:3]
centena = numero[1:1]
milhar = numero[0:0]

#Saída:
print(f'A unidade é: [{unidade}]')
print(f'A dezena é: [{dezena}]')
print(f'A centena é: [{centena}]')
print(f'O milhar é: [{milhar}]')
print('-'*50)