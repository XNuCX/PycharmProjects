def cache(func):
    log = {}
    def wrapper(n):
        log[n] = func(n)
        return
    return wrapper
@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
