#-faça um progama que leia um numero inteiro e mostre na tela o seu antecessor e o seu sucessor.
n1 = int(input('me fale um numero?'))
suc  = n1 + 1
ant  = n1 - 1

print(f'o antecessor do seu numero é {ant}')
print(f'e o seu sucessor é {suc}')
#-----------------------------------------------

#-Crie um algoritimo que leia um numero e mostre o seu dobro, triplo, e a raiz quadrada:
print('me fale um numero:')
n = int(input(''))
print('...')

mul = n*2
rai = n**(1/2)
tri = n*3
print(f'o seu dobro é {mul}')
print(f'a raiz dela é {rai:2}')
print(f'o seu triplo é {tri}')
#-----------------------------------------------

#-Desenvolva um progama que leia as suas notas e mostre a sua media
print("me fale suas notas dentro dos ultimos 5 meses")
m1 = float(input('1°mês'))
m2 = float(input('2°mês'))
m3 = float(input('3°mês'))
m4 = float(input('4°mês'))
m5 = float(input('5°mês'))
R = (m1 + m2 + m3 + m4 + m5)/5
 
print(f'a sua média é de {R}')
#-----------------------------------------------

#-Escreva um progama que leia um valor em metros e o exiba em centimetros e melimetros.
print('me fale quantos metros existe a sua rua:')
met = int(input(''))

cet = met * 100
mil = met * 1000
print('...')
print(f'a sua rua em centimetros, tem, "{(met*100)}" centimetros')
print('...')
input(f'que saber quantos ela tem em melimetros? da uma >enter')
print('...')
print(f'a sua rua em melimetros, tem "{(met*1000)}" melímetros')
#-----------------------------------------------

#-Faça um progama que leia um numero inteiro qualquer, e mostre na tela a sua tabuada.
print('me fale um nuemero qualquer')

n = int(input('>'))
r1 = n*1
r2 = n*2
r3 = n*3
r4 = n*4
r5 = n*5
r6 = n*6
r7 = n*7
r8 = n*8
r9 = n*9
r10= n*10
W  = ('='*15)
M  = ('='*12)

print(f'{W}\n{n}x1={r1} \n{n}x2={r2} \n{n}x3={r3} \n{n}x4={r4} \n{n}x5={r5} \n{n}x5={r6} \n{n}x7={r7} \n{n}x8={r8} \n{n}x9={r9} \n{n}x10={r10}\n{M}')
#-----------------------------------------------

#-Crie um progama que leia quantos dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar
print('me fale quantos voce tem em dinheiro?')
n = float(input('R$'))

dol = n * 5.26

print(f'você pode comprar cerca de {dol:5} doláres')
#-----------------------------------------------

#-Faça um progama que leia a largura e a altura de uma parede em metros, calcule a sua aréa e a quantidade de tinta necessaria para pintala sabendo que  cada litro de tinta pinta um area de 2m²
print('me fale a altura da parede e alargura? ')
ALT = float(input('altura:'))
LAR = float(input('largura:'))

ARE = ALT * LAR

LIT = ARE/2

print(f' o tanto de tinta que vamos usar vai ser de {LIT} litro(s)')
#-----------------------------------------------

#-Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
print('me fale o preço do produto?')
PRE = float(input('>'))
print('e a porcetagem que vai abaixar:')
PRO = float(input('>'))

D = PRE*PRO/100

DES = PRE - D

print(f'baixando o preço que vai ficar é {DES}')
#-----------------------------------------------

#faça um algoritimo que leia o salario de um fucionario de um funcionario e mostre seu novo salario com 15% de aumento.
print('qual é seu novo salario:')
SAL = float(input('=>'))

print('quantos porcentos vai ser aumentado:')
AUM =float(input('=>'))

POR = SAL*AUM/100

SAL = SAL + POR

print(f'você vai começar cerca R${SAL}')
#-----------------------------------------------
