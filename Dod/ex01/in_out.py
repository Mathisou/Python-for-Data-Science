def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x raised to the power of x."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a function that applies the given function to x and updates x"""
    try:
        if not callable(function):
            raise TypeError("The second argument must be a callable function.")

        def inner() -> float:
            """Applies the function to x and updates x."""
            nonlocal x
            x = function(x)
            return x
        return inner
    except TypeError as e:
        print(f"Error: {e}")
        return None
