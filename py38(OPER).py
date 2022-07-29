A = 5+3*2
print(f'A = {A}') # o resul é == 11
# ordem de precedencia 1°=>(), 2°=>** 3°=>*,/,% e // 4°=> + e -
 
B = 3*5+4**2
print(f'B = {B}') # o resultado é == 31

C = 3*(5+4)**2
print(f'C = {C}') # o resultado é == 243

D = 52**52
print(f'D = {D}')

E = pow(52,2)
print(f'E = {E}')

F = 25**(1/2)
print(f'F = {F}')

print('='*20)

nome = input('me fale seu nome:? ') # para quebrar alinha é necessario usar o => '\n', e para elas é necessario usar o end=''
print(f'olás prazer em te conhecer{nome:=^20}!')

print('='*20)

G = 4/3

print(f'G = {G:.3}')
