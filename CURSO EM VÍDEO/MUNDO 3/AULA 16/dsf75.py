'''
Desenvolva um programa que leia quatro valores pelo
teclado e guarde-os em uma tupla. No final, mostre:

a) Quantas vezes apareceu o valor 9
b)Em que posição foi digitado o primeiro valor 3.
c) Quais foram os numeros pares.
'''
tup = (int(input("Digite um número: ")), 
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),
       int(input("Digite o último número: ")))

print(f"Você digitou os valores {tup}")
 
if 9 in tup:
    cont = tup.count(9)
    print(f"O número 9 apareceu {cont} vezes!")
else:
    print("O número 9 não apareceu nenhuma vez!")

if 3 in tup:
    print(f"O número 3 está na {tup.index(3)+1}ª posição")
else:
    print("O número 3 não foi digitado nenhuma vez!")

print("Os valores pares digitados foram: ", end= "")
for num in tup:
    if num % 2 == 0:
        print(num, end= " ")
