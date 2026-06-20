import numpy as np

from PIL import Image


# Convert Image to RGB
def convert_to_rgb(
        image
):

    return image.convert(
        "RGB"
    )


# Resize Large Images
def resize_image(
        image,
        max_dimension=800
):

    image.thumbnail(
        (
            max_dimension,
            max_dimension
        )
    )

    return image


# Convert Image to NumPy Array
def image_to_array(
        image
):

    return np.array(
        image
    )


# Convert NumPy Array to Image
def array_to_image(
        image_array
):

    return Image.fromarray(
        image_array.astype(
            np.uint8
        )
    )