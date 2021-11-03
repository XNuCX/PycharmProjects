class Test:
    def __init__(self,b, *args):
        self.b = b
        self.a = self.function(args)
        for a1 in args:
            self.a = a1
    staticmethod
    def function(self, args):
        if args:
            return args[0]
        else:
            return
b= Test(0)
print(b.a)
print(b.b)