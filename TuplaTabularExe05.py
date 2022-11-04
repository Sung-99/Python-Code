ListaTabular = tuple( ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20,'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90))

print('-'*40)
print('Listagem de preços'.center(40))
print('-'*40)
for c in range(len(ListaTabular)):
    if c == 0:
        print(f"{ListaTabular[c]:.<30}R$    {ListaTabular[c+1]}")
    if c % 2 == 0 and c > 0:
        print(f"{ListaTabular[c]:.<30}R$    {ListaTabular[c-1]}")
x = str()
