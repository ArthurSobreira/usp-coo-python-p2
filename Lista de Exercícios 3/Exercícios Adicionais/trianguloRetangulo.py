class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        my_list = [self.a, self.b, self.c]
        hip = max(my_list)
        my_list.remove(hip)
        cat1 = my_list[0]
        cat2 = my_list[1]
        if (hip ** 2) == ((cat1 ** 2) + (cat2 ** 2)):
            return True
        else:
            return False
