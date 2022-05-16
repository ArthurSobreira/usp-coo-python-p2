def ordenada(lista):
    tam = (len(lista)) - 1
    cont_t = 0
    for c in range(tam):
        prox = c + 1
        if lista[c] <= lista[prox]:
            cont_t += 1

    if cont_t == tam:
        return True
    else:
        return False
