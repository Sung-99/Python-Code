import random
x =(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
           random.randint(1, 10), random.randint(1, 10))
print(f'Números: {x[0:]}')
print(f'Números ordenados: {sorted(x)}')
print(f'Menor Número: {sorted(x)[0]}')
print(f'Maior Numero: {sorted(x)[4]}')

