def ft_filter(func, iterable: list) -> list:
    """
    Filters elements from an iterable using a given function.
    """
    if func is None:
        return [elem for elem in iterable if elem]
    return [elem for elem in iterable if func(elem)]
