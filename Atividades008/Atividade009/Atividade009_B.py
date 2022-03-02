# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data início: 03/12/2021
# Término: 08/12/2021
# Exercício B

#Importado biblioteca:
import os

#Limpando terminal:
os.system('cls')

#Título:
print('-'*50)
print('Elaborando um Programa com Tuplas:')
print('Check List de Atividades Diárias (Materiais Escolares).')
print('='*50)

#Declaração:
itensEscola = ('mochila', 'caderno', 'estojo', 'uniforme', 'tenis', 'chave', 'guarda-chuva', 'passagem')

#Operações:
print(f'Itens necessários para ir a escola: {itensEscola}')
listaEscola = list(itensEscola)
saida = ['exit']
print('-'*50)

while (True):

    print('Para sair digite "exit"!')
    item1 = str(input('Digite um item que voce já pegou: ')).lower()
    if item1 in listaEscola:
        listaEscola.remove(item1)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item1 in saida:
        print('Voce encerrou o programa!')
        exit()
        

    else:
     item1 not in listaEscola
     print('O item não está na lista!')
     print()

while (True):

    print('Para sair digite "exit"!')
    item2 = str(input('Digite o segundo item que voce já pegou: ')).lower()
    if item2 in listaEscola:
        listaEscola.remove(item2)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item2 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item2 not in listaEscola
        print('O item não está na lista!')
        print()

while (True):

    print('Para sair digite "exit"!')
    item3 = str(input('Digite um item que voce já pegou: ')).lower()
    if item3 in listaEscola:
        listaEscola.remove(item3)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item3 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item3 not in listaEscola
        print('O item não está na lista!')
        print()

while (True):

    print('Para sair digite "exit"!')
    item4 = str(input('Digite um item que voce já pegou: ')).lower()
    if item4 in listaEscola:
        listaEscola.remove(item4)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item4 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item4 not in listaEscola
        print('O item não está na lista!')
        print()

while (True):

    print('Para sair digite "exit"!')
    item5 = str(input('Digite um item que voce já pegou: ')).lower()
    if item5 in listaEscola:
        listaEscola.remove(item5)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item5 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item5 not in listaEscola
        print('O item não está na lista!')
        print()

while (True):

    print('Para sair digite "exit"!')
    item6 = str(input('Digite um item que voce já pegou: ')).lower()
    if item6 in listaEscola:
        listaEscola.remove(item6)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item6 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item6 not in listaEscola
        print('O item não está na lista!')
        print()

while (True):

    print('Para sair digite "exit"!')
    item7 = str(input('Digite um item que voce já pegou: ')).lower()
    if item7 in listaEscola:
        listaEscola.remove(item7)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item7 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item7 not in listaEscola
        print('O item não está na lista!')
        print()

while (True):

    print('Para sair digite "exit"!')
    item8 = str(input('Digite um item que voce já pegou: ')).lower()
    if item8 in listaEscola:
        listaEscola.remove(item8)
        print(f'Ainda faltam: {listaEscola}')
        print()
        break

    elif item8 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item8 not in listaEscola
        print('O item não está na lista!')
        print()
        
        

print()
print('-'*50)
print('Parabens, voce ja pegou tudo!')
print('='*50)
print()