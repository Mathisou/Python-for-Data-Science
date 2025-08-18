import sys

try:
    if len(sys.argv) == 1:
        exit()

    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    print("I'm Even." if number % 2 == 0 else "I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")