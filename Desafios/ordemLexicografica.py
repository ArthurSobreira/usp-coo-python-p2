def menor_string(list_strings):
    my_list = []
    for c in list_strings:
        my_list.append(c.strip().lower())

    list_tam = []
    for i in my_list:
        som = 0
        for j in i:
            som += ord(j)
        list_tam.append(som)
    men = list_tam.index(min(list_tam))

    return my_list[men]


