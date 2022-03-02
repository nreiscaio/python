#Curso Técnico de Informática
#Autor: Caio Nascimento
#Data início: 10/11/2021
#Término: 12/11/2021
#Exercicio D

#Importando as bibliotecas:
import os

#Limpando o terminal:
os.system('cls')

#Título:
print('-'*50)
print('PROGRAMA QUE LEIA UMA FRASE E DEPOIS MOSTRE NA TELA:')
print('FRASE EM MINÚSCULO')
print('FRASE EM MAIÚSCULO')
print('QUANTIDADE DE CARACTERES NA FRASE')
print('QUANTAS LETRAS TEM A 2º PALAVRA NA FRASE')
print('='*50)

#Entrada de Dados:
frase = str(input('Digite a frase:'))
letra = str(input('Digite a letra que deseja ver a ocorrência:'))

print('='*50)

#Declaração:
minusculo = frase.lower()
maiusculo = frase.upper()
quantidadeCaracteres = len(frase)
ocorrencia = frase.count(letra, 0, )

#Saída:
print(f'A frase "{frase}" em minúsculo: {minusculo}')
print(f'A frase "{frase}" em maiúsculo: {maiusculo}')
print('-'*50)
print(f'A frase "{frase}" tem {quantidadeCaracteres} caracteres!')
print('-'*50)
print(f'Na frase "{frase}" a letra selecionada aparece {ocorrencia} vezes!')
print('-'*50)
print('FIM DO PROGRAMA')
print('='*50)