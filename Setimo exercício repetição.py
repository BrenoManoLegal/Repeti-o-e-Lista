print("Digite 5 números:")
numeros = []
for i in range(5):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

maior_numero = max(numeros)

print("O maior número é:", maior_numero)