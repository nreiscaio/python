#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 04/11/2021
#Data Termino: 04/11/2021

print('-'*50)
print('PROGRAMA PARA CALCULAR A EQUAÇÃO x² -6x + 5 ')
print('='*50)

#Entrada:
a = int(input('Informe o valor de "a": '))
b = int(input('Informe o valor de "b": '))
c = int(input('Informe o valor de "c": '))

#Valor de Delta
delta = (b ** 2) - (4 * a * c)

#Execução:
soluçãox = (-b + (delta ** (1/2))) / (2 * a)
soluçãox2 = (-b - (delta ** (1/2))) / (2 * a)

#Saida:
print('-'*50)
print('CALCULO DE RAIZ QUADRADA')
print('='*50)
print(soluçãox,soluçãox2)
print('-'*50)
print('FIM DO PROGRAMA')
print('-'*50)