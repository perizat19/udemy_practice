# First example
def decorator_fn(original_fn):
    def wrapper_fn(*args, **kwargs):
        print("Before")

        result = original_fn(*args, **kwargs)

        print("After")

        return result

    return wrapper_fn


@decorator_fn
def my_fn(a, b):
    print("This is a function")
    return (a, b)

res = my_fn(100, 2)
print(res)


# Second example
def decorator_fn(original_fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of {arg} is {type(arg)}",
                                "All args should be int or float!")
        result = original_fn(*args, **kwargs)
        return result
    
    return wrapper


@decorator_fn
def sum_nums(a, b):
    return a + b


print(sum_nums(10, 23))


# Example with dictionary checking

def decorator_fn(original_fn):
    def wrapper(*args, **kwargs):
        for arg in [*args, *kwargs.values()]:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise ValueError(f"Type of {arg} is {type(arg)}",
                                "All args should be int or float!")
        result = original_fn(*args, **kwargs)
        return result
    
    return wrapper


@decorator_fn
def sum_nums(a, b):
    return a + b

try:
    print(sum_nums(10, 23))
    print(sum_nums('abc', '12'))
except ValueError as e:
    print(e)


# User authentication
def is_authenticated():
    return False 


def check_user_authentication(fn):
    def wrapper(*args, **kwargs):
        if is_authenticated():
            return fn(*args, **kwargs)
        else:
            raise Exception("User is NOT authenticated")
    return wrapper


@check_user_authentication
def send_message():
    print("You are enrolled to the system!")


try:
    send_message()
except Exception as e:
    print(e)