import matplotlib.pyplot as plt
import numpy as np


def display_image(image):
    """
    Display the image using matplotlib.
    """
    print(f"The shape of image is: {image.shape}")
    print(image)
    try:
        plt.imshow(image)
        plt.show()
    except KeyboardInterrupt:
        print("Image display interrupted by user.")


def ft_invert(array):
    """Invert the colors of the image."""
    if array is not None:
        new_array = array.copy()
        for x in range(array.shape[1]):
            for y in range(array.shape[0]):
                new_array[y, x] = 255 - array[y, x]
        display_image(new_array)
    return array


def ft_red(array):
    """Convert the image to red."""
    if array is not None:
        new_array = array.copy()
        for x in range(array.shape[1]):
            for y in range(array.shape[0]):
                new_array[y, x][1] = 0
                new_array[y, x][2] = 0
        display_image(new_array)
    return array


def ft_green(array):
    """Convert the image to green."""
    if array is not None:
        new_array = array.copy()
        for x in range(array.shape[1]):
            for y in range(array.shape[0]):
                new_array[y, x][0] = 0
                new_array[y, x][2] = 0
        display_image(new_array)
    return array


def ft_blue(array):
    """Convert the image to blue."""
    if array is not None:
        new_array = array.copy()
        for x in range(array.shape[1]):
            for y in range(array.shape[0]):
                new_array[y, x][0] = 0
                new_array[y, x][1] = 0
        display_image(new_array)
    return array


def ft_grey(array):
    """Convert the image to grayscale."""
    if array is not None:
        for x in range(array.shape[1]):
            for y in range(array.shape[0]):
                grey_value = int(np.mean(array[y, x][:3]))
                array[y, x] = [grey_value, grey_value, grey_value]
        display_image(array)
    return array
