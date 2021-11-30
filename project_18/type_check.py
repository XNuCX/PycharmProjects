def type_check(type_to_check):
    def decorator(func):
        def wrapper(a):
            if type(a) == type_to_check:
                return func(a)
            else:
                return f"Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
