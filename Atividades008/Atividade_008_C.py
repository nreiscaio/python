# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data início: 29/11/2021
# Término: 29/11/2021
# Exercício C

# Importado biblioteca
import os


# Limpando terminal
os.system('cls')

#Título:
print('-'*50)
print('Programa que procure na lista os numeros e produza o que foi pedido')
print('='*50)
print()

#Entrada de Dados:
listaNumeros = int(input('Digite a lista de números que deseja:'))
print('='*50)
print()

#Saída Formatada:
print(f'Os números são: {listaNumeros}')
print()
print(f'O primeiro intervalo é: {listaNumeros[0:9]}')
print(f'O segundo intervalo é: {listaNumeros[7:13]}')
print()
print(f'Números par: {listaNumeros[1:15:2]}')
print(f'Números impar: {listaNumeros[0:15:2]}')
print('='*50)
print()
print('Fim do Programa')
print('='*50)
