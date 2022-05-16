def dimensoes(matriz):
    lin = 0
    colu = 0
    for c in range(len(matriz)):
        lin += 1
        colu = len(matriz[c])

    return lin, colu


def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        matriz_soma = []
        for c in range(len(m1)):
            lin = []
            for i in range(len(m1[0])):
                lin.append(m1[c][i] + m2[c][i])
            matriz_soma.append(lin)
        return matriz_soma
    else:
        return False
