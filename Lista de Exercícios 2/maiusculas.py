def maiusculas(frase):
    list_upper = []
    for c in frase:
        if (c == c.upper()) and (c.isalpha()):
            list_upper.append(c)
    val = ''.join(list_upper)

    return val
