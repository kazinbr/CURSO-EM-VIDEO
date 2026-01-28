'''
Faça um prorama que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.
'''

n = 0

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('---' * 10)
    for i in range(1, 11):
        m = n * i
        print(f'{n} x {i} = {m}')
    print('---' * 10)    
print('OPERAÇÃO TABUADA ENCERRADA, Volte sempre!')