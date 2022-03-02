#Curso Técnico de Informática
#Autor: Caio N
#Data de Início: 26/10/2021
#Término: 26/10/2021
#Estudo de Variáveis 

#Declaraçâo
nome = str(input('qual o seu nome'))
dataNascimento = int(input('em que ano voce nasceu'))
rg = int(input('qual o seu registro geral'))
cpf = int(input('qual seu numer do cpf'))

#Endereço
rua = str(input('qual sua rua')) 
numero = int(input('qual o numero da sua casa'))
complemento = str(input('ponto de referencia'))
cep = int(input('nao obrigatorio'))
cidade = str(input('cidade onde voce nasceu'))
estado = str(input('estado onde voce nasceu'))
pais = str(input('nacionalidade'))

#Saída
print('-'*50)
print("Atividade Cadastro")
print('='*50)
print("Seu nome é................: ", nome)
print("Ano de nascimento.........: ", dataNascimento)
print("Seu RG é..................: ", rg)
print("Seu CPF é.................: ", cpf)
print("Seu endereço é............: ", rua, numero, complemento, cep, cidade, estado, pais)
print('='*50)
print('FIM DO PROGRAMA')
print('-'*50)