lista_de_numeros = [10.0, 15.5, 7.3, 22.8,-4564.45]

for i in range(len(lista_de_numeros)):
    for j in range(i +1, len(lista_de_numeros)):
        if lista_de_numeros[i] > lista_de_numeros[j]:
            lista_de_numeros[i], lista_de_numeros[j] = lista_de_numeros[j], lista_de_numeros[i]
print(lista_de_numeros)