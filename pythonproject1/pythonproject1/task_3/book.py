class Book:
    # В библиотеке False
    checked_out = False

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def check_out(self):
        if not self.checked_out:
            print('Выдаём книгу абоненту')
            self.checked_out = True
        else:
            print('Книга находится у абонента')

    def check_in(self):
        if self.checked_out:
            print('Принимаем книгу у абонента')
            self.checked_out = False
        else:
            print('Книга в наличии')


a = Book('Капитанская дочка', 'А. С. Пушкин')
a.check_in()
a.check_out()
a.check_in()
a.check_out()
