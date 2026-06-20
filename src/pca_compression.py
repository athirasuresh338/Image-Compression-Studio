import numpy as np

from sklearn.decomposition import PCA


# Compress a Single Color Channel Using PCA
def compress_channel_pca(
        channel,
        n_components
):
    
    # Determine Valid Number of Components
    max_components = min(
        channel.shape
    )

    n_components = min(
        n_components,
        max_components
    )

    # Create PCA Model
    pca = PCA(
        n_components=n_components
    )

    # Reduce Dimensions
    transformed = pca.fit_transform(
        channel
    )

    # Reconstruct Original Channel
    reconstructed = (
        pca.inverse_transform(
            transformed
        )
    )

    return reconstructed


# PCA Image Compression
def compress_image_pca(
        image_array,
        n_components
):

    # Split RGB Channels
    red_channel = image_array[:, :, 0]

    green_channel = image_array[:, :, 1]

    blue_channel = image_array[:, :, 2]

    # Compress Red Channel
    red_compressed = (
        compress_channel_pca(
            red_channel,
            n_components
        )
    )

    # Compress Green Channel
    green_compressed = (
        compress_channel_pca(
            green_channel,
            n_components
        )
    )

    # Compress Blue Channel
    blue_compressed = (
        compress_channel_pca(
            blue_channel,
            n_components
        )
    )

    # Reconstruct RGB Image
    compressed_image = np.stack(
        [
            red_compressed,
            green_compressed,
            blue_compressed
        ],
        axis=2
    )

    # Ensure Valid Pixel Values
    compressed_image = np.clip(
        compressed_image,
        0,
        255
    )

    # Return Image in Valid RGB Format
    return compressed_image.astype(
        np.uint8
    )