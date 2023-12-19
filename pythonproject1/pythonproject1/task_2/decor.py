def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'{result} руб.'
    return wrapper

@currency
def price_calculation(price, tax):
    return price*(1+tax)


# price_calculation = currency(price_calculation)
print(price_calculation(100, 0.05))


def result(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'Результат вычислений: {result}'
    return wrapper
@result
def twice(a):
    return 2*a
@result
def square(a):
    return a**2


print(twice(4))
print(square(66))
