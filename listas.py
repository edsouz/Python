lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [7, 8, 9]

print(lista1, "\n")
print(lista2, "\n")
print(lista1 + lista2, '\n')

for i in lista1:
    print(i, '\n')


lista1.append(7)
lista2.append(10)

print(lista1)
print(lista2)

print("\n")

lista1.pop()
lista2.pop(1)

print(lista1, '\n')
print(lista2, '\n')

lista1.reverse()
print(lista1, '\n')

lista1.sort()
print(lista1, '\n')

x = lista1.index(3)

print('O índice do item 3 é ', x, '\n')

lista2.remove(7)

print(lista2)



