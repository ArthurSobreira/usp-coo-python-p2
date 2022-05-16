def busca(lista, elemento):
    prim = 0
    ult = len(lista) - 1
    while prim <= ult:
        meio = (prim + ult) // 2
        print(meio)
        if lista[meio] == elemento:
            return meio
        else:
            if elemento < lista[meio]:
                ult = meio - 1
            else:
                prim = meio + 1

    return False
