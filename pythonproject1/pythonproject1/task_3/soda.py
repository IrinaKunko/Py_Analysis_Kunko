class Soda:

    def __init__(self, add=None):
        self.add = add

    def show_my_drink(self):
        if self.add:
            print('Газировка и', self.add)
        else:
            print('Обычная газировка')


soda = Soda()
soda.show_my_drink()
lemonsoda = Soda('lemon')
lemonsoda.show_my_drink()
