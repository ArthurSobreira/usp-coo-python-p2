def men(list_nomes):
    menor = list_nomes[0]
    for c in list_nomes:
        if len(c) < len(menor):
            menor = c

    return menor


def menor_nome(nomes):
    my_list = []
    for c in nomes:
        my_list.append(c.strip().capitalize())

    return men(my_list)

