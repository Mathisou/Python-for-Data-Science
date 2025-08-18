import matplotlib.pyplot as plt
from load_image import ft_load


def display_image(image):
    """
    Display the image using matplotlib.
    """
    plt.imshow(image, cmap='gray')
    plt.show()


def main(xmin=100, xmax=500, ymin=100, ymax=500):
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
    zoomed_image = image[ymin:ymax, xmin:xmax, 0:1]
    print(f"New shape after slicing: {zoomed_image.shape}")
    print(zoomed_image)
    display_image(zoomed_image)
    return zoomed_image


if __name__ == "__main__":
    main()
