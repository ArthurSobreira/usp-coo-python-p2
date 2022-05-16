def busca(lista, elemento):
    if elemento in lista:
        for c in range(len(lista)):
            if lista[c] == elemento:
                return c
    else:
        return False
