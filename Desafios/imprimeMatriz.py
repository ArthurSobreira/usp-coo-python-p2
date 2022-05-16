def cria_matriz(num_lin, num_cul, val):
    matriz = []
    for c in range(num_lin):
        linha = []
        for i in range(num_cul):
            linha.append(val)
        matriz.append(linha)

    return matriz


def imprime_matriz(matriz):
    for c in range(len(matriz)):
        for i in matriz[c]:
            print(f'{i} ', end=' ')
        print()


def main():
    imprime_matriz(cria_matriz(3, 2, 0))


if __name__ == '__main__':
    main()
