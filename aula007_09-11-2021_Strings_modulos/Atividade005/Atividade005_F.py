# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data início: 10/11/2021
# Término: 10/11/2021
# Exercício_a: Raíz quadrada

# Importando as bibliotecas
import os
from random import randint


# Limpando o terminal
os.system('cls')

# Título
print('-' * 50)
print('PROGRAMA PARA SORTEAR UM NÚMERO')
print('=' * 50)

#Entrada de dados e declarações
numero = int(input('Digite um número entre 1 e 20: '))
npc = randint(1, 3) #npc: non-player character

# Validação
if ( numero < 0 or numero > 3):
    print('Número inválido!')

else: # Tudo certo
    print(f'Sua escolha foi: {numero}')
    print(f'NPC escolheu: {npc}')
    print('-'*50)

    # Condicional do resultado
    if (numero == npc):
        print('- Você ganhou!!!')
    else:
        print('- Você perdeu!')

# Saída
print('-'*50)
print('Fim do Programa!')
print('-'*50)
print()