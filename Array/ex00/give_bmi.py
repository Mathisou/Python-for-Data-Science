import numpy as np
import sys


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """ Calculate the Body Mass Index (BMI) for given height and weight lists."""
    try:
        if len(height) != len(weight):
            raise ValueError("Height and weight lists must have the same length.")
        if not height or not weight:
            raise ValueError("Height and weight lists cannot be empty.")
        if any(h <= 0 for h in height) or any(w <= 0 for w in weight):
            raise ValueError("Height and weight must be positive values.")
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("Height and weight must be lists.")
        if not all(isinstance(h, (int, float)) for h in height) or not all(isinstance(w, (int, float)) for w in weight):
            raise TypeError("Height and weight must contain only integers or floats.")
        height = np.array(height)
        weight = np.array(weight)
        bmi = weight / (height ** 2)
        return bmi.tolist()
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        sys.exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check if each BMI value exceeds the specified limit."""
    try:
        if not isinstance(bmi, list) or not all(isinstance(b, (int, float)) for b in bmi):
            raise TypeError("BMI must be a list of integers or floats.")
        if not isinstance(limit, (int, float)):
            raise TypeError("Limit must be an integer or float.")
        if limit <= 0:
            raise ValueError("Limit must be a positive value.")
        bmi = np.array(bmi)
        return (bmi > limit).tolist()
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)
