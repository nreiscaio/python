#Curso Tecnico de Informatica
#Autor: Caio Nascimento
#Data inicio: 04/11/2021
#Data Termino: 04/11/2021

print('-'*50)
print('PROGRAMA PARA CALCULAR ANO BISSEXTO')
print('='*50)

#Entrada de Dados
ano = int(input('Informe um ano qualquer: '))

#Condicional
if (ano <= 0):
    print('Ano inválido!')
elif(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

print('-'*50)