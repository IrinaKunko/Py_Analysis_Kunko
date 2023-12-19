class Data:

    def __new__(cls, *args, **kwargs):
        print('state fetching')
        return super().__new__(cls)

    def __init__(self, l):
        self.l = l
        print('data processing', self.l)


obj1 = Data([7, 'ascd', True, [1, 2, 3]])
obj2 = Data([5.6, 'asda', (1, 2, 3)])

