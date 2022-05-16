def ordena(lista):
    tam = len(lista)
    for c in range(tam):
        men = c
        for i in range(c + 1, tam):
            if lista[men] > lista[i]:
                men = i

        lista[c], lista[men] = lista[men], lista[c]

    return lista

