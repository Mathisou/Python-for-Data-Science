from PIL import Image
import numpy as np
import os


def ft_load(path: str):
    """
    Load an image, prints its format, and its pixelscontent in RGB format.
    """
    try:
        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError(
                "Unsupported file format. Only .jpg and .jpeg are allowed."
            )
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file {path} does not exist.")
        img = Image.open(path)
        img = np.array(img)
        print(f"The shape of image is: {img.shape}")
        return img
    except (ValueError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")
        return None
