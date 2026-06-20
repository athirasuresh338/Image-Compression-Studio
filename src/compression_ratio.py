# K-Means Compression Ratio
def calculate_kmeans_ratio(
        image_array,
        k
):

    # Image Dimensions
    height, width, channels = (
        image_array.shape
    )

    # Original Storage
    original_size = (
        height
        *
        width
        *
        channels
    )

    # Compressed Storage
    compressed_size = (
        (k * channels)
        +
        (height * width)
    )

    # Compression Ratio
    ratio = (
        original_size
        /
        compressed_size
    )

    return ratio


# PCA Compression Ratio
def calculate_pca_ratio(
        image_array,
        n_components
):

    # Image Dimensions
    height, width, channels = (
        image_array.shape
    )

    # Original Storage
    original_size = (
        height
        *
        width
        *
        channels
    )

    # Compressed Storage Per Channel
    compressed_channel = (
        (height * n_components)
        +
        (n_components * width)
    )

    compressed_size = (
        channels
        *
        compressed_channel
    )

    # Compression Ratio
    ratio = (
        original_size
        /
        compressed_size
    )

    return ratio


# SVD Compression Ratio
def calculate_svd_ratio(
        image_array,
        rank
):

    # Image Dimensions
    height, width, channels = (
        image_array.shape
    )

    # Original Storage
    original_size = (
        height
        *
        width
        *
        channels
    )

    # Compressed Storage Per Channel
    compressed_channel = (
        (height * rank)
        +
        rank
        +
        (rank * width)
    )

    compressed_size = (
        channels
        *
        compressed_channel
    )

    # Compression Ratio
    ratio = (
        original_size
        /
        compressed_size
    )

    return ratio