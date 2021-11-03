class Test:
    def __init__(self, a):
        self._a = a

    @property
    def a(self):
        if self._a == 0:
            raise ValueError
        else:
            return self._a
    @a.setter
    def a(self, value):
        self._a = value

b= Test(1)

print(b.a)

b.a = 0
print(b.a)