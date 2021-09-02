from functools import wraps

def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper

@type_logger
def calc_cube(*nums):
    return list(map(lambda x: x**3, nums))

test = calc_cube(5,3)
print(test)