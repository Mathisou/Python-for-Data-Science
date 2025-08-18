import sys
from ft_filter import ft_filter


def check_args():
    """Check command line arguments for validity."""
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    if not sys.argv[2].isdigit():
        raise AssertionError("the arguments are bad")
    for char in sys.argv[1]:
        if not char.isalpha() and not char.isdigit() and char != ' ':
            raise AssertionError("the arguments are bad")


def main():
    """Filter words in a string based on their length."""
    try:
        check_args()
        text = sys.argv[1]
        n = int(sys.argv[2])
        filtered = ft_filter(lambda word: len(word) > n, text.split())
        print(filtered)
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
