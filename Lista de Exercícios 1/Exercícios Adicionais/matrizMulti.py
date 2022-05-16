def sao_multiplicaveis(m1, m2):
    if (len(m1) == len(m2[0])) or (len(m2) == len(m1[0])):
        return True
    else:
        return False


ma1 = [[1, 2, 3], [4]]
ma2 = [[2, 3], [5, 6, 7]]
print(sao_multiplicaveis(ma1, ma2))
