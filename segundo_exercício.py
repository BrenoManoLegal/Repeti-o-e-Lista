
ListaNumerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ListaInvertida = []
for i in range(0, len(ListaNumerica)):
    ListaInvertida.append(ListaNumerica[len(ListaNumerica)-1])
    ListaNumerica.pop()
print("Inversão:",ListaInvertida)



