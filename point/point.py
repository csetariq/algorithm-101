import math
import random


class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return repr((self.name, self.id))


x = Student("Rijja", 1)
y = Student("Nyla", 2)
a = [x, y]

def x2(x):
    return x ** 2

def s_name(q):
    return q.name


def s_id(s):
    return s.id

print(s_name(x))

print(sorted(a, key=s_name))

print(sorted(a, key=lambda s: s.id))

x.name = "Mathew"
print(a)


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    # def set_x(self, x):
    #     if x > 0:
    #         self.__x = x

    def get_y(self):
        return self.__y

    def distance(self, blah):
        x2 = math.pow((self.__x - blah.__x), 2)
        y2 = math.pow((self.__y - blah.__y), 2)
        return math.sqrt(x2 + y2)

    def is_part_of(self, plane):
        print(plane.get_a())

    def __repr__(self):
        return repr((self.__x, self.__y))

class Plane:
    def __init__(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

# def distance(a, b):
#     x2 = math.pow((a.get_x() - b.get_x()), 2)
#     y2 = math.pow((a.get_y() - b.get_y()), 2)
#     return math.sqrt(x2 + y2)

a = Point(1, 1)
b = Point(5, 1)

print(a.is_part_of(Plane(2)))
print(a.distance(b))

l = []
for i in range(10):
    x = random.randrange(20)
    y = random.randrange(20)
    l.append(Point(x, y))

print(l)

t = Point(19, 19)

def distance_to_t(one_from_the_list):
    return t.distance(one_from_the_list)

l.sort(key=distance_to_t)

k = 4

result = l[0:k]

for p in l:
    print(f'distance from {p} to {t}: {distance_to_t(p)}')

print(result)