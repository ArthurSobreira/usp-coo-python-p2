def primeiro_lex(lista):
    men = lista[0]
    for c in lista:
        if c[0] < men:
            men = c

    return men


