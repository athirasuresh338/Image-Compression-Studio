import numpy as np

from skimage.metrics import (
    structural_similarity
)


# Peak Signal-to-Noise Ratio (PSNR)
def calculate_psnr(
        original_image,
        compressed_image
):

    mse = np.mean(
        (
            original_image.astype(float)
            -
            compressed_image.astype(float)
        ) ** 2
    )

    # Images Are Identical
    if mse == 0:

        return float("inf")

    max_pixel = 255.0

    psnr = (
        20 * np.log10(max_pixel)
        -
        10 * np.log10(mse)
    )

    return psnr


# Structural Similarity Index (SSIM)
def calculate_ssim(
        original_image,
        compressed_image
):

    score = structural_similarity(
        original_image,
        compressed_image,
        channel_axis=2,
        data_range=255
    )

    return score


# PSNR Quality Interpretation
def get_psnr_quality(
        psnr
):

    if psnr >= 40:

        return (
            "Excellent - Very little "
            "quality loss."
        )

    elif psnr >= 30:

        return (
            "Good - Most visual "
            "details are preserved."
        )

    elif psnr >= 20:

        return (
            "Moderate - Noticeable "
            "quality loss."
        )

    else:

        return (
            "Poor - Significant "
            "quality degradation."
        )


# SSIM Similarity Interpretation
def get_ssim_interpretation(
        ssim
):

    if ssim >= 0.95:

        return (
            "Almost Identical "
            "to the original image."
        )

    elif ssim >= 0.85:

        return (
            "Very Similar "
            "to the original image."
        )

    elif ssim >= 0.70:

        return (
            "Noticeably Different "
            "from the original image."
        )

    else:

        return (
            "Significantly Different "
            "from the original image."
        )