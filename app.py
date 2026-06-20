import streamlit as st

from PIL import Image

from src.utils import (
    convert_to_rgb,
    resize_image,
    image_to_array,
    array_to_image
)

from src.kmeans_compression import (
    compress_image_kmeans
)

from src.pca_compression import (
    compress_image_pca
)

from src.svd_compression import (
    compress_image_svd
)

from src.metrics import (
    calculate_psnr,
    calculate_ssim,
    get_psnr_quality,
    get_ssim_interpretation
)

from src.compression_ratio import (
    calculate_kmeans_ratio,
    calculate_pca_ratio,
    calculate_svd_ratio
)


# Page Configuration
st.set_page_config(
    page_title="Image Compression Studio",
    layout="wide"
)


# Session State
if "compressed_image" not in st.session_state:

    st.session_state.compressed_image = None

if "results" not in st.session_state:

    st.session_state.results = None

if "last_uploaded_file" not in st.session_state:

    st.session_state.last_uploaded_file = None


# Header
st.title(
    "Image Compression Studio"
)

st.write(
    """
    Explore image compression using
    K-Means Clustering, PCA, and SVD.

    Adjust compression parameters and observe
    how image quality changes through visual
    comparison and evaluation metrics.
    """
)

st.divider()


# Controls
control_col1, control_col2, control_col3 = (
    st.columns(3)
)

with control_col1:

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )

    # Detect New Upload
    if (
        uploaded_file is not None
        and
        st.session_state.get(
            "last_uploaded_file"
        ) != uploaded_file.name
    ):

        st.session_state.compressed_image = None

        st.session_state.results = None

        st.session_state.last_uploaded_file = (
            uploaded_file.name
        )

with control_col2:

    algorithm = st.selectbox(
        "Compression Method",
        [
            "K-Means",
            "PCA",
            "SVD"
        ]
    )

with control_col3:

    parameter = st.slider(
        "Parameter",
        min_value=1,
        max_value=100,
        value=25
    )


# Image Uploaded
if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    )

    image = convert_to_rgb(
        image
    )

    image = resize_image(
        image
    )

    image_array = image_to_array(
        image
    )

    st.divider()

    # Run Button
    center_col1, center_col2, center_col3 = (
        st.columns([3, 1, 3])
    )

    with center_col2:

        run_compression = st.button(
            "Run Compression",
            use_container_width=True
        )

    # Run Compression
    if run_compression:

        if algorithm == "K-Means":

            compressed_array = (
                compress_image_kmeans(
                    image_array,
                    parameter
                )
            )

            compression_ratio = (
                calculate_kmeans_ratio(
                    image_array,
                    parameter
                )
            )

        elif algorithm == "PCA":

            compressed_array = (
                compress_image_pca(
                    image_array,
                    parameter
                )
            )

            compression_ratio = (
                calculate_pca_ratio(
                    image_array,
                    parameter
                )
            )

        else:

            compressed_array = (
                compress_image_svd(
                    image_array,
                    parameter
                )
            )

            compression_ratio = (
                calculate_svd_ratio(
                    image_array,
                    parameter
                )
            )

        compressed_image = (
            array_to_image(
                compressed_array
            )
        )

        psnr = (
            calculate_psnr(
                image_array,
                compressed_array
            )
        )

        ssim = (
            calculate_ssim(
                image_array,
                compressed_array
            )
        )

        st.session_state.compressed_image = (
            compressed_image
        )

        st.session_state.results = {

            "compression_ratio":
                compression_ratio,

            "psnr":
                psnr,

            "ssim":
                ssim,

            "psnr_quality":
                get_psnr_quality(
                    psnr
                ),

            "ssim_quality":
                get_ssim_interpretation(
                    ssim
                )
        }

    # Image Comparison
    image_col1, image_col2 = (
        st.columns(2)
    )

    with image_col1:

        st.subheader(
            "Original Image"
        )

        st.image(
            image,
            width="stretch"
        )

    with image_col2:

        st.subheader(
            "Compressed Image"
        )

        if (
            st.session_state.compressed_image
            is not None
        ):

            st.image(
                st.session_state.compressed_image,
                width="stretch"
            )

    # Results
    if st.session_state.results is not None:

        st.divider()

        st.subheader(
            "Compression Results"
        )

        metric_col1, metric_col2, metric_col3 = (
            st.columns(3)
        )

        with metric_col1:

            st.metric(
                "Compression Ratio",
                f"{st.session_state.results['compression_ratio']:.2f}x"
            )

            st.caption(
                f"The compressed representation "
                f"requires approximately "
                f"{st.session_state.results['compression_ratio']:.2f}× "
                f"less information than the "
                f"original image."
            )

        with metric_col2:

            st.metric(
                "PSNR",
                f"{st.session_state.results['psnr']:.2f} dB"
            )

            st.caption(
                st.session_state.results[
                    "psnr_quality"
                ]
            )

        with metric_col3:

            st.metric(
                "SSIM",
                f"{st.session_state.results['ssim']:.4f}"
            )

            st.caption(
                st.session_state.results[
                    "ssim_quality"
                ]
            )

