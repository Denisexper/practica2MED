nuumeros = [4, 5, 6, 4, 1, 8, 9, 6, 3, 2]
pares = []
impares = []
for numero in nuumeros:
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    print("lista: ", nuumeros)
    print("numeros pares: ", pares)
    print("numeros impares: ", impares)