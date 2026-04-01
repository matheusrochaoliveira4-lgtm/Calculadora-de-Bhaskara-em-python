#formula de baskara

import math
print ("baskara")

a = int(input())

if a == 0:
    print('não há divisão por zero, terminar!!')
else:
    b = int(input())
    c = int(input())
    delta = math.pow(b,2)-4*a*c
    print(f'{delta:.3f}')
    if delta <0:
        print ('não existem raizes reais')
    elif delta == 0:
        x = (-b , math.sqrt(delta))/2*a
        print(f'x = {x:.1f}')
    else:
        x = (-b + math.sqrt(delta))/(2*a)
        x1 = (-b - math.sqrt(delta))/(2*a)
        print(f'x: = {x:.1f}')
        print(f'x1: = {x1:.1f}')
