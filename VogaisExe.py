Palavra = ("Vamo","embora","Daqui")

for cont in Palavra:
    print(f"\nNa palavra '{cont}' temos as vogais: ", end="")
    for x in range(0, len(cont)):
        if cont[x].lower() in 'aeiou' and x < len(cont):
            print(cont[x], end="")


