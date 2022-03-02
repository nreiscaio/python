#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 09/11/2021
#Data Termino: 09/11/2021
#Estudo de Variáveis: Módulos em Python

import math

import os
os.system('cls')

print('-'*50)
print('ESTUDO DA BIBLIOTECA MATH')
print('-'*50)

#Arredondamentos de número para cima ou para baixo
#Entrada de Dados
numeroDecimal = float(input('Entre com um numero decimal: '))

#Cálculos
arredondarParaCima = math.ceil(numeroDecimal)
arredondarParaBaixo =  math.floor(numeroDecimal)

#Saída
print('-'*50)
print(f'O numero {numeroDecimal} arredondado para cima é: {arredondarParaCima}')
print(f'o numero {numeroDecimal} arredondado para baixo é: {arredondarParaBaixo}')
print('-'*50)