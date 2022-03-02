#Curso Técnico de Informática
#Autor: Caio Nascimento
#Data início: 10/11/2021
#Término: 12/11/2021
#Exercicio H

#Importando as bibliotecas:
import os

#Limpando o terminal:
os.system('cls')

#Titulo:
print('-'*50)
print('PROGRAMA PARA LER NOME DO ALUNO E MOSTRE:')
print('VEZES QUE A LETRA "O" APARECE')
print('POSIÇÃO EM QUE APARECE PELA 1ª VEZ')
print('='*50)

#Entrada de Dados:
nome = str(input('Digite o nome do aluno:'))
letra = str(input('Digite a letra que deseja ver a ocorrência:'))

#Declaração:
quantidadeCaracteres = len(nome)
ocorrencia = nome.count(letra, 0, )


#Saida:
print(f'A frase "{nome}" tem {quantidadeCaracteres} caracteres!')
print('-'*50)
print(f'Na frase "{nome}" a letra selecionada aparece {ocorrencia} vezes!')
print('-'*50)
print('FIM DO PROGRAMA')
print('='*50)