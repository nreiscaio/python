# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data início: 10/11/2021
# Término: 10/11/2021
# Exercício_a: Raíz quadrada

# Importando as bibliotecas
import os
import math


# Limpando o terminal
os.system('cls')

# Título
print('-' * 50)
print('CÁLCULO DE EQUAÇÃO DO 2º GRAU')
print('=' * 50)

#Entrada de dados
a = int(input('Informe o valor de "a": '))
b = int(input('Informe o valor de "a": '))
c = int(input('Informe o valor de "c": '))

#Calculando as Raízes
x1 = ((-b) + (math.sqrt((math.pow(b, 2) - (4 * a * c))))) / 2 * a
x2 = ((-b) - (math.sqrt((math.pow(b, 2) - (4 * a * c))))) / 2 * a

#Saída
print('-' * 50)
print(f'As raízes da equação são ({x1}, {x2}) ')
print('='*50)
print()