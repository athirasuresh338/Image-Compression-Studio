import numpy as np


# Compress a Single Color Channel Using SVD
def compress_channel_svd(
        channel,
        rank
):

    # Perform Singular Value Decomposition
    U, S, VT = np.linalg.svd(
        channel,
        full_matrices=False
    )

    # Determine Valid Rank
    max_rank = min(
        channel.shape
    )

    rank = min(
        rank,
        max_rank
    )

    # Keep Only Selected Rank
    U_reduced = U[:, :rank]

    S_reduced = S[:rank]

    VT_reduced = VT[:rank, :]

    # Reconstruct Channel
    reconstructed = (
        U_reduced
        @ np.diag(S_reduced)
        @ VT_reduced
    )

    return reconstructed


# SVD Image Compression
def compress_image_svd(
        image_array,
        rank
):

    # Split RGB Channels
    red_channel = image_array[:, :, 0]

    green_channel = image_array[:, :, 1]

    blue_channel = image_array[:, :, 2]

    # Compress Red Channel
    red_compressed = (
        compress_channel_svd(
            red_channel,
            rank
        )
    )

    # Compress Green Channel
    green_compressed = (
        compress_channel_svd(
            green_channel,
            rank
        )
    )

    # Compress Blue Channel
    blue_compressed = (
        compress_channel_svd(
            blue_channel,
            rank
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