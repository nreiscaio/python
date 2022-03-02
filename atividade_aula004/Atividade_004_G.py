#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 04/11/2021
#Data Termino: 04/11/2021

print('-'*50)
print('PROGRAMA PARA CALCULAR EXISTêNCIA DE UM TRIÂNGULO')
print('-'*50)

#Entrada de Dados
a = int(input('Informe o segmento "a": '))
b = int(input('Informe o segmento "b": '))
c = int(input('Informe o segmento "c": '))

#Condicional
if (a <= 0 or b <= 0 or c <= 0):
    print('Valor de segmento inválido')
elif ((a < (b + c)) and (b < (a + c)) and 9< (a + c)):
    print(f'{a} + {b} + {c}, formam um triângulo!')
else:
    print(f'{a} + {b} + {c}, não formam um triângulo!')

print('-'*50)          