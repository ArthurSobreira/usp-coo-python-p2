def imprime_matriz(matriz):
    for c in matriz:
        lim = len(c)
        for i in range(lim):
            if i != (lim - 1):
                print(c[i], end=' ')
            else:
                print(c[i], end='')
        print()

