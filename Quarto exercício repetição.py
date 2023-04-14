populacaoA = 80000
taxaCrescimentoA = 0.03 # 3%

populacaoB = 200000
taxaCrescimentoB = 0.015 # 1.5%

anos = 0

while populacaoA < populacaoB:
    populacaoA += populacaoA * taxaCrescimentoA
    populacaoB += populacaoB * taxaCrescimentoB
    anos += 1

print("Anos necessários:", anos)