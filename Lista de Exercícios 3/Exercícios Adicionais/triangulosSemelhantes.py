class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, tri):
        k = self.a / tri.a
        if (self.b / tri.b == k) and (self.c / tri.c == k):
            return True
        else:
            return False

