import os
import random


class Matrix:
    def __init__(self, r, c, v = None):
        self.r = r
        self.c = c
        self.v = v
        if not v:
            self.v = []
            self.__populate__()

    def __populate__(self):
        for i in range(self.r):
            row = [random.randint(0, 20) for x in range(self.c)]
            self.v.append(row)

    def add(self, other):
        v = []
        for i in range(self.r):
            row = []
            for j in range(self.c):
                row.append(self.v[i][j] + other.v[i][j])
            v.append(row)

        return Matrix(self.r, self.c, v)

    def __repr__(self):
        str_v = []
        for row in self.v:
            str_v.append(",\t".join([str(x) for x in row]))
        return os.linesep.join(str_v)

a = Matrix(3, 4)
b = Matrix(3, 4)
print('a')
print(a)
print('b')
print(b)
print('sum')
print(a.add(b))