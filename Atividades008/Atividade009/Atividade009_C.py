# Curso Técnico de Informática
# Autor: Caio Nascimento
# Data início: 03/12/2021
# Término: 08/12/2021
# Exercício C

#declarar a entrada de dados, em uma variavel.
#antes do verificação dos mesmos em if.
#adicionar item a item para verificação
#'quais itens o aluno trouxe?' 'esta dentro do padrao?' 'se sim, esta liberado' 
#'se nao aparece uma mensagem'
#entrada de dados (variavel)
#verificação (variavel 'if')
#repetição
#modo de saída
#fechamneto
#fim

#Suponha que uma escola vá fazer uma verificação dos materiais dos alunos
#Se eles levaram todos os materiais necessarios e/ou permitidos

# Importado biblioteca
import os

# Limpando terminal
os.system('cls')

#Título:
print('-'*50)
print('Elaborando um programa com Sets:')
print('Verificação de materiais.')
print('='*50)
print()

#Declaração:
itensObrigatorios = {'mochila', 'caderno', 'estojo', 'uniforme', 'tenis', 'chave', 'guarda-chuva', 'passagem'}
sim = ['S', 's']
nao = ['F', 'f']
saida = ['exit']
tudo = ['S', 'F', 's', 'f','exit']
itensListados = set()
mochila = ['mochila']
caderno = ['caderno']
estojo = ['estojo']
uniforme = ['uniforme']
tenis = ['tenis']
chave = ['chave']
guardaChuva = ['guarda-chuva']
passagem = ['passagem']

#Condicionais:
while (True):

    print('"Mochila"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item1 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item1 in sim:
        itensObrigatorios.remove('mochila')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(mochila)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item1 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item1 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item1 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

while (True):

    print('"Caderno"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item2 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item2 in sim:
        itensObrigatorios.remove('caderno')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(caderno)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item2 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item2 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item2 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

while (True):

    print('"Estojo"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item3 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item3 in sim:
        itensObrigatorios.remove('estojo')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(estojo)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item1 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item1 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item1 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

while (True):

    print('"Caderno"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item4 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item4 in sim:
        itensObrigatorios.remove('uniforme')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(caderno)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item4 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item4 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item4 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

while (True):

    print('"Tenis"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item5 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item5 in sim:
        itensObrigatorios.remove('tenis')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(tenis)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item5 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item5 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item5 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

while (True):

    print('"Caderno"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item6 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item6 in sim:
        itensObrigatorios.remove('chave')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(chave)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item6 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item6 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item6 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

while (True):

    print('"Guarda-Chuva"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item7 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item7 in sim:
        itensObrigatorios.remove('guarda-chuva')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(guardaChuva)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item7 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item7 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item7 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

while (True):

    print('"Caderno"')
    print('Pressione "S" se o objeto faz parte do material ou "N" se não faz!')
    print('Digite "exit" caso queira encerrar o programa!')
    item8 = str(input('Digite "S", "F" ou "exit": ')).lower()
    if item8 in sim:
        itensObrigatorios.remove('passagem')
        print('Ainda falta a verificação dos seguintes itens:')
        print(itensObrigatorios)
        itensListados.update(passagem)
        print(f'Itens ja verificados: {itensListados}')
        print('Prossiga com a vistoria: ')
        print()
        break

    elif item8 not in tudo:
        print('Erro! Digite novamente!')
        continue

    elif item8 in saida:
        print('Voce encerrou o programa!')
        exit()

    else:
        item8 in nao
        print('O item não faz parte do material necessário!')
        print('Remova-o do aluno.')
        print(f'Os itens necessários são: {itensObrigatorios}')
        print()

print()
print('-'*50)
print('Parabens, voce ja verificou tudo!')
print('='*50)
print()