class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b