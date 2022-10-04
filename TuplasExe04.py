
z = tuple((int(input("Digite o primeiro valor:")),
           int(input("Digite o segundo valor:")),
           int(input("Digite o terceiro valor:")),
           int(input("Digite o quarto valor:"))))
print(f"O numero 9 apareceu {z.count(9)} vezes")
if 3 in z:
    print(f"O numero 3 apareceu na {z.index(3)} posicao")
else:
    print(f"O numero 3 nao existe nessa tupla")
print("Os numeros pares sao:", end='')
for c in range(4):
    if z[c] % 2 == 0:
        print(z[c], end=' ')
