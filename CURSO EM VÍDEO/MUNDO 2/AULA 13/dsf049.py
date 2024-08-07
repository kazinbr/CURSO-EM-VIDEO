'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o 
usuário escolher, só que agora usando um laço for.
'''
n1 = int(input('Escolha um número: '))

print(f'Tabuada do {n1}: ')
for i in range(1,11):
    r = n1 * i
    print(f'{n1} x {i} = {r}')
