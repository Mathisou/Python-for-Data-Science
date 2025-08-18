import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Takes a 2D array, prints its shape, and returns a truncated version using slicing.
    """
    try:
        if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
            raise TypeError("family must be a 2D list")
        row_length = len(family[0]) if family else 0
        if any(len(row) != row_length for row in family):
            raise ValueError("All rows must have the same size")
        arr = np.array(family)
        print(f"My shape is : {arr.shape}")
        sliced = arr[start:end]
        print(f"My new shape is : ({sliced.shape}")
        return sliced.tolist()
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return []
