class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        print(f'({self.real + other.real},{self.imaginary + other.imaginary}j)')
        # return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __repr__(self):
        return repr((self.real, f'{self.imaginary}j'))


# a = complex(5, 3)
# b = complex(3, 5)

a = Complex(5, 3)
b = Complex(3, 5)

print(a)

c = a + b

print(c)
