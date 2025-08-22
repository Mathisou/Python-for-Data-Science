import sys


MORSE_CODE_DICT = {' ': '/', 'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----'}


def check_args():
    """Check if the number of arguments is correct and if the input is valid"""
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    if not all(char.isalnum() or char == ' ' for char in sys.argv[1]):
        raise AssertionError("the arguments are bad")


def main():
    """Convert the input text to Morse code."""
    try:
        check_args()
        text = sys.argv[1].upper()
        morse_code = ' '.join(MORSE_CODE_DICT.get(char) for char in text)
        print(morse_code)
    except AssertionError as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
