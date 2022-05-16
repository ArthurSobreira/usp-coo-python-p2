def conta_letras(frase, contar='vogais'):
    list_vog = []
    list_con = []
    for c in frase:
        if c.isalpha():
            c = c.lower()
            if c in 'aeiou':
                list_vog.append(c)
            else:
                list_con.append(c)

    if contar == 'consoantes':
        return len(list_con)
    else:
        return len(list_vog)

