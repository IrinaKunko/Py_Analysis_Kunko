class DataBase:

    __instance = None

    # Такой метод выделяет память только для обного объекта
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        # super() переопределяет выполнение метода
        # Метод new всегда возвращает созданный объект
        return cls.__instance

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user} {self.password} {self.port}')

    @staticmethod
    def close():
        print('Закрытие соединения с БД')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))
db2.connect()