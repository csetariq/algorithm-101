import array


class List:
    def __init__(self, capacity):
        self._capacity = capacity
        self._i = 0
        self._arr = array.array('i', [0] * capacity)

    def insert(self, x):
        if self._i < self._capacity:
            self._arr[self._i] = x
            self._i += 1
            return True
        return False

    def search(self, y) -> int:
        for i in range(self._i):
            if self._arr[i] == y:
                return i
        return -1

    def remove(self, z) -> bool:
        t = self.search(z)

        if t == -1:
            return False

        for i in range(t, self._i - 1):
            self._arr[i] = self._arr[i + 1]

        self._i -= 1
        return True

    def display(self):
        for i in range(self._i):
            print(self._arr[i], end=' ')
        print()


l = List(4)
print(l.insert(1))
print(l.insert(3))
print(l.insert(4))
print(l.insert(7))

print(l.search(1))
print(l.search(7))

print(l.remove(1))
l.display()

print(l.remove(1))
l.display()

print(l.remove(3))
l.display()

print(l.remove(4))
l.display()

print(l.insert(11))
print(l.insert(12))
print(l.insert(13))
print(l.insert(14))

l.display()