def bubble_sort(lista):
    tam = len(lista)
    for c in range(tam - 1, 0, -1):
        change = False
        for i in range(c):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                print(lista)
                change = True
        if not change:
            return lista

    return lista
