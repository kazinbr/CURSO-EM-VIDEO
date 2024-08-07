import math
c1 = float(input('Qual o comprimento do cateto oposto? '))
c2 =float(input('Qual o comprimento do cateto adjacente: ')) 
print(f'O comprimento do lado da hipotenusa é {math.hypot(c1, c2):.1f}')
