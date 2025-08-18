import sys


def count_print(value: int, key: str) -> None:
    """Print the count and character type label."""
    print(value, key)


def count_characters(text: str) -> dict:
    """Count how many types of characters are present in the string."""

    char_type = {
        "upper letters": 0,
        "lower letters": 0,
        "punctuation marks": 0,
        "spaces": 0,
        "digits": 0
    }
    for char in text:
        if 'a' <= char <= 'z':
            char_type["lower letters"] += 1
        elif 'A' <= char <= 'Z':
            char_type["upper letters"] += 1
        elif '0' <= char <= '9':
            char_type["digits"] += 1
        elif char == ' ':
            char_type["spaces"] += 1
        else:
            char_type["punctuation marks"] += 1
    return char_type


def main():
    """Reads a string from command line and prints character counts."""
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            text = input("What is the text to count?\n")

        count = count_characters(text)
        print(f"The text contains {len(text)} characters:")
        for key, value in count.items():
            count_print(value, key)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
