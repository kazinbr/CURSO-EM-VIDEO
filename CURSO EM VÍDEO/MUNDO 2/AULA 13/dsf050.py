'''
Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.
'''
par = []

for i in range(1, 7):
    n1 = int(input(f'Digite o {i} valor: '))
    
    if n1 % 2 == 0:
        par.append(n1)
if par == []:
    print("Não foi informado nenhum número par!")        
else:
    print(f'A soma de todos os números pares digitados é {sum(par)}')
