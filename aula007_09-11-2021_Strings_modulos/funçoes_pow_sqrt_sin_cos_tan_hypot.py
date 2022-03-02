#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 09/11/2021
#Data Termino: 09/11/2021
#Estudo de Variáveis: Módulos em Python

#Importando toda a biblioteca da função
import math
import os
os.system('cls')

#Declarções
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5 #Cateto oposto
ca = 10 #Cateto Adjacente

#Cálculos
potencia = math.pow(base, expoente)
raizQuadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo)) #Observação: função sin() só trabalha com rad

#Saída
print(f'O numero {base} elevado a {expoente} tem resultado: {potencia}')
print(f'A raiz quadrada de {radicando} é: {raizQuadrada}')
print(f'O seno do ângulo {angulo}º é: {seno:.1f}')
print('-'*50)