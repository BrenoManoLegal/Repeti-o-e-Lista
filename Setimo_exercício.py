# Leitura dos números inteiros
vetor = []
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    vetor.append(num)

# Cálculo da soma e multiplicação dos números
soma = sum(vetor)
multiplicar = 1
for num in vetor:
    multiplicar *= num

# Impressão dos resultados
print("Números digitados: ", vetor)
print("Soma dos números: ", soma)
print("Multiplicação dos números: ", multiplicar)