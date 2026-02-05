'''
Faça um prorama que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('---' * 10)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('---' * 10)    
print('OPERAÇÃO TABUADA ENCERRADA, Volte sempre!')