'''
Crie um programa que leia vários números
inteiro pelo teclado. O programa só vai parar
quando o usuário diitar o valor 999, que é a condição de parada.
No final, motre quantos números foram digitados e qual foi a soma entre eles
'''
v = n = s = 0

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    v += 1
    s += n
print(f'A soma dos {v} valores é {s}')
