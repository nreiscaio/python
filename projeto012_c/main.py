#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 28/10/2021
#Data Termino: 28/10/2021
#Atividade 003: Exercicio I = Tabuada de mutiplicação.

from ast import Break, While
import os
from conversor import Conversor

os.system('cls')

#Entrada:
print('-'*50)
print('CONVERSOR DE REAIS EM DOLAR')
print('='*50)

#Entrada de dados:
dolar = 1
euro = 2
libra = 3


digito = int(input('Insira qual conversao você deseja fazer: '))
a = float(input('Por favor, insira um valor em reais: '))

valor = Conversor

resultado = valor.conversorDolar(a)
resulatdo2 = valor.conversorEuro(a)
resultado3 = valor.conversorLibra(a)


while True:
    if digito == 1:
        print(f'R${a} vale U${resultado:.4f}')

        break

    elif digito == 2:
        print(f'R${a} vale U${resulatdo2:.4f}')

        break

    elif digito == 3:
        print(f'R${a} vale U${resultado3:.4f}')

        break

    else:
        print('Nâo encontrado')