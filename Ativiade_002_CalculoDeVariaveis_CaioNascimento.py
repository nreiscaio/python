#Atividades Aula 002

#Entrada dados
a = int(input('Entre com o primeiro valor: 10'))
b = int(input('Entre com o primeiro valor: 2'))

#Soma
soma = a + b
#Subtração
subtraçao = a - b
#Produto
produto = a * b
#Divisão
divisao = a / b
#Potencia
potencia = a ** b
#Divisão Inteira
divisaoInteiros = a // b
#Resto da Divisão
restoDivisão = a % b
#Raiz Quadrada
raizQuadradaa = a ** (1/2)
raizQuadradab = b ** (1/2)
#Raiz Cubica
raizCubicaa = a ** (1/3)
raizCubicab = b ** (1/3)

#Saída
print('-'*50)
print('ESTUDO DE OPERADORES ARITMETICOS')
print('=*50')
print(f'O valor de {a} + {b} = {soma}')
print(f'O valor de {a} - {b} = {subtraçao}')
print(f'O valor de {a} * {b} = {produto}')
print(f'O valor de {a} / {b} = {divisao}')
print(f'O valor de {a} ** {b} = {potencia}')
print(f'O valor de {a} // {b} = {divisaoInteiros}')
print(f'O valor de {a} % {b} = {restoDivisão}')
print(f'O valor de {a} ** (1/2) = {raizQuadradaa:.2f}')
print(f'O valor de {b} ** (1/2) = {raizQuadradab:.2F}')
print(f'O valor de {a} ** (1/3) = {raizCubicaa:.2f}')
print(f'O valor de {b} ** (1/3) = {raizCubicab:.2f}')
print(f'='*50)
print('FIM DO PROGRAMA')
print('-'*50)