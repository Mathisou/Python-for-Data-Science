from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def display_image(image):
    """
    Display the image using matplotlib.
    """
    try:
        plt.imshow(image, cmap='gray')
        plt.show()
    except KeyboardInterrupt:
        print("Image display interrupted by user.")


def zoom(xmin=450, xmax=850, ymin=150, ymax=550):
    """
    Zooms into a specified region of the image.
    """

    image = ft_load("animal.jpeg")
    if image is None:
        print("No image to zoom.")
        return None

    height, width, _ = image.shape
    xmin = max(0, min(xmin, width - 1))
    xmax = max(0, min(xmax, width - 1))
    ymin = max(0, min(ymin, height - 1))
    ymax = max(0, min(ymax, height - 1))
    if xmin >= xmax or ymin >= ymax:
        print("Invalid zoom coordinates.")
        return None
    if xmax - xmin != ymax - ymin:
        print("Zoom region must be square.")
        return None
    zoomed_image = image[ymin:ymax, xmin:xmax, 0:1]
    print(f"The shape of image is: {zoomed_image.shape}")
    print(zoomed_image)
    return zoomed_image


def transpose_image(img):
    """
    Transpose the zoomed image.
    """
    transpose = []
    for x in range(img.shape[1]):
        row = []
        for y in range(img.shape[0]):
            row.append(img[y][x][0])
        transpose.append(row)
    return np.array(transpose)


def main():
    """
    Main function to execute the zoom and transpose operations.
    """
    img = zoom()
    if img is not None:
        transposed_img = transpose_image(img)
        print(f"New shape after Transpose: {transposed_img.shape}")
        print(transposed_img)
        display_image(transposed_img)
    else:
        print("Zoom operation failed.")


if __name__ == "__main__":
    main()
