import numpy as np

from sklearn.cluster import MiniBatchKMeans


# K-Means Image Compression
def compress_image_kmeans(
        image_array,
        k
):

    # Get Image Dimensions
    height, width, channels = image_array.shape

    # Convert Image into Pixel Matrix
    pixels = image_array.reshape(
        -1,
        3
    )

    # Train MiniBatch K-Means Model
    kmeans = MiniBatchKMeans(
        n_clusters=k,
        random_state=42,
        batch_size=2048
    )

    # Assign Each Pixel to a Cluster
    labels = kmeans.fit_predict(
        pixels
    )

    # Replace Pixels with Cluster Centroids
    compressed_pixels = (
        kmeans.cluster_centers_[labels]
    )

    # Reconstruct Compressed Image
    compressed_image = (
        compressed_pixels.reshape(
            height,
            width,
            channels
        )
    )

    # Return Image in Valid RGB Format
    return compressed_image.astype(
        np.uint8
    )