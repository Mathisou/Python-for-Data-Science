def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calculates and prints various statistics based on the provided arguments.
    """

    if args and not all(isinstance(arg, (int, float)) for arg in args):
        print("Invalid data type in args. Only int or float are allowed.")
        return

    def median():
        """Calculates the median of the provided arguments."""
        return sorted(args)[len(args) // 2]

    def mean():
        """Calculates the mean of the provided arguments."""
        return sum(args) / len(args)

    def quartile():
        """
        Calculates the first and third quartiles of the provided arguments.
        """
        return [
            float(sorted(args)[int(len(args) // 4)]),
            float(sorted(args)[int(len(args) // 1.5)])
        ]

    def std():
        """Calculates the standard deviation of the provided arguments."""
        return var() ** 0.5

    def var():
        """Calculates the variance of the provided arguments."""
        return sum((x - mean()) ** 2 for x in args) / len(args)

    for stat in kwargs.values():
        if not args:
            print("ERROR")
        else:
            if stat == "mean":
                print(f"mean : {mean()}")
            elif stat == "median":
                print(f"median : {median()}")
            elif stat == "quartile":
                print(f"quartile : {quartile()}")
            elif stat == "std":
                print(f"std : {std()}")
            elif stat == "var":
                print(f"var : {var()}")
