def lista_grande(n):
    import random
    my_list = []
    for c in range(n):
        my_list.append(random.choice(range(1000)))

    return my_list
