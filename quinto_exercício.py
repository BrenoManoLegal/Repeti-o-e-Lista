Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Impares = []
Pares = []
for i in Numeros:
    if Numeros[i-1]%2:
        Impares.append(Numeros[i-1])
    else:
        Pares.append(Numeros[i-1])

print("Numeros", Numeros)
print('Impares', Impares)
print('Pares', Pares)

