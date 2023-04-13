vogais= ['a', 'e', 'i', 'o', 'u']
consoante = ["b", "r", "n", "e", "o", "h", "j", "k", "l", "m"]
consoantes= []
consoantes= 0
contador= 0
for i in consoante:
    if not consoante[contador] in vogais:
        consoante+= 1
        consoantes.append(consoantes[contador])
    contador += 1
    print("consoantes:", consoantes)
    print("Outras consoantes:", consoante)







