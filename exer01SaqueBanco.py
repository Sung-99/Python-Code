conferePedido = bool(True)
total = int(0)
print('='*10, '-'*10)
print("Banco saudavel")
print('='*10, '-'*10)
print("*" * 30)
while conferePedido:
    resp = str(input("Deseja sacar ?"))
    total = 0
    if resp in "nNnaoNao":
        conferePedido = False
        print("*" * 30)
        print("Banco saudavel Agradece")
    elif resp in "sSsimSim":
        x = int(input("Quanto Deseja sacar ?"))
        total = x // 50
        print("{} unidades de 50".format(total))
        x = x - (total*50)
        total = x // 20
        print("{} unidades de 20".format(total))
        x = x - (total*20)
        total = x // 10
        print("{} unidades de 10".format(total))
        x = x - (total*10)
        total = x // 5
        print("{} unidades de 5".format(total))
        x = x - (total*5)
        total = x // 1
        print("{} unidades de 1".format(total))
