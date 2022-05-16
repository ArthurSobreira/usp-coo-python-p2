def dimensoes(matriz):
    lin = 0
    colu = 0
    for c in range(len(matriz)):
        lin += 1
        colu = len(matriz[c])
    print(f'{lin}X{colu}')

    return lin, colu


ma = [[1, 2], [3, 4]]
dimensoes(ma)
