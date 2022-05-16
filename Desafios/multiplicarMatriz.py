def multi_matriz(ma, mb):
    lin_ma, col_ma = len(ma), len(ma[0])
    lin_mb, col_mb = len(mb), len(mb[0])
    assert col_ma == lin_mb

    mc = []
    for lin in range(lin_ma):
        mc.append([])
        for col in range(col_mb):
            mc[lin].append(0)
            for i in range(col_ma):
                mc[lin][col] += ma[lin][i] * mb[i][col]

    return mc


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(multi_matriz(A, B))

