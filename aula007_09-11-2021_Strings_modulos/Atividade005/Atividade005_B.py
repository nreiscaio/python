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
print('CALCULANDO DIVISÃO COM ARREDONDAMENTO: FUNÇÃO')
print('=' * 50)

#declarações
arredondarCima = 0
arredondarBaixo = 0

#Entrada de dados
numerador = int(input('Entre com o numerador: '))
denominador = int(input('Entre com o denominador: '))
print('-'*50)

# Validação
if (numerador == 0):
    #Saída
    print(f'A divisão de {numerador} pelo {denominador} é: {numerador}')

elif (denominador == 0):
    # Saída
    print('-'*50)
    print('Não existe divisão por 0!')

else: # Deu tudo certo
    divisao = numerador / denominador

    #Condicional
    if (divisao % 2 == 0):
        print(f'A divisão de {numerador} pelo {denominador} é: {divisao}')

    else: # Se a divisão não for inteira
        arredondarCima = math.ceil(divisao)
        arredondarBaixo = math.floor(divisao)

        # Saída
        print('-' * 50)
        print(f'A divisão de {numerador} por {denominador}' +
              f' arredondado para cima é: {arredondarCima}')
        print(f'A divisão de {numerador} por {denominador}' +
              f' arredondado para baixo é: {arredondarBaixo}')
        print('-' * 50)

print('Fim do programa!')
print('-'*50)
print()