def insertion_sort(lista):
    tam = len(lista)
    for c in range(tam - 1):
        men = c
        for i in range(c + 1, tam):
            if lista[i] < lista[men]:
                men = i

        lista[c], lista[men] = lista[men], lista[c]

    return lista
