class calculator:
    """
    A simple calculator class that performs
    arithmetic operations on a vector.
    """

    def __init__(self, vector):
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a object value to each element of the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a object value."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, object) -> None:
        """Subtract a object value from each element of the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a object value."""
        try:
            if object == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.vector = [x / object for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
