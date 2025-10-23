def log(filename=None):
    """Декоратор для логирования выполнения функции, ее результатов и ошибок"""

    def wrapper(function):
        def inner(*args, **kwargs):
            messages = []
            try:
                messages.append(f"{function.__name__} start")
                result = function(*args, **kwargs)
                messages.append(f"{function.__name__} result: {result}")
            except Exception as e:
                messages.append(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise
            finally:
                messages.append(f"{function.__name__} end")
                if filename:
                    with open(filename, "w") as f:
                        for message in messages:
                            f.write(message + "\n")
                else:
                    print("\n".join(messages))

            return result

        return inner

    return wrapper
