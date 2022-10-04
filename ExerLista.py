num = [2, 3, 5, 4]
print(num)
num[2] = 9
print(num)
num.insert(0, 5)
print(num)
num.pop(2)
print(num)
num.remove(5)
print(num)
num.append(int(input("digite um valor:")))
print(num)
for c, v in enumerate(num):
    print(f"Na posição {c} está o valor {v}")
numCopia = num[:]
numCopia[1] = 11
print(num)
print(numCopia)
