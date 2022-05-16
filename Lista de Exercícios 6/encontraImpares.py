def encontra_impares(lista):
    if len(lista) == 0:
        return []
    x = lista.pop(0)
    if x % 2 != 0:
        return [x] + encontra_impares(lista)
    return encontra_impares(lista)

