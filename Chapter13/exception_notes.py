def func(x, y):
    return x / y

def secret_function(number):
    try:
        func(10_000, number)
    except ArithmeticError as e:
        e.add_note("A note to help with debugging")
        raise

secret_function(0)
