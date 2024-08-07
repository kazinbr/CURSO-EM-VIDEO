''' 
Desenvolva uma lógica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''
peso = float(input('Quanto você pesa? '))
alt = float(input('Qual a sua altura? '))

imc = peso / (alt ** 2)

if imc < 18.5:
    print(f'Você tem {peso}Kg e sua altura é de {alt}\nSeu IMC é {imc}, você está abaixo do peso!!')
elif 18.5 <= imc < 25:
     print(f'Você tem {peso}Kg e sua altura é de {alt}\nSeu IMC é {imc}, você está no peso ideal!!')
elif 25 <= imc < 30:
     print(f'Você tem {peso}Kg e sua altura é de {alt}\nSeu IMC é {imc}, você está sobrepeso!!')
elif 30 <= imc < 40:
     print(f'Você tem {peso}Kg e sua altura é de {alt}\nSeu IMC é {imc}, você está obeso!!')
else:
     print(f'Você tem {peso}Kg e sua altura é de {alt}\nSeu IMC é {imc}, você está com obesidade mórbida!!')
