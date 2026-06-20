# Image Compression Studio

An interactive Streamlit application for exploring and comparing image compression techniques using **K-Means Clustering**, **Principal Component Analysis (PCA)**, and **Singular Value Decomposition (SVD)**.

The application allows users to upload an image, adjust compression parameters, visualize compression results, and evaluate image quality using quantitative metrics.

---

## Features

* Upload and compress images using K-Means, PCA, and SVD
* Adjustable compression parameters
* Side-by-side comparison of original and compressed images
* Theoretical compression ratio analysis
* PSNR and SSIM quality evaluation
* Interactive Streamlit interface

---

## Compression Techniques

### K-Means Clustering

Reduces the number of colors in an image by grouping similar pixels into clusters and replacing them with cluster centroids.

### Principal Component Analysis (PCA)

Compresses images through dimensionality reduction while preserving the most important information.

### Singular Value Decomposition (SVD)

Approximates images using lower-rank matrix representations to reduce information requirements.

---

## Evaluation Metrics

### Compression Ratio

Measures the theoretical reduction in information representation achieved by the selected compression algorithm.

### PSNR (Peak Signal-to-Noise Ratio)

Measures reconstruction quality between the original and compressed image.

| PSNR Value | Quality   |
| ---------- | --------- |
| > 40 dB    | Excellent |
| 30 – 40 dB | Good      |
| 20 – 30 dB | Moderate  |
| < 20 dB    | Poor      |

### SSIM (Structural Similarity Index)

Measures structural similarity between the original and compressed image.

| SSIM Value  | Similarity              |
| ----------- | ----------------------- |
| 0.95 – 1.00 | Almost Identical        |
| 0.85 – 0.95 | Very Similar            |
| 0.70 – 0.85 | Noticeably Different    |
| < 0.70      | Significantly Different |

---

## Technologies Used

* Python
* Streamlit
* NumPy
* Pillow (PIL)
* Scikit-Learn
* Scikit-Image

---

## Project Structure

```text
Image_Compression_Studio/
│
├── app.py
│
├── src/
│   ├── __init__.py
│   ├── compression_ratio.py
│   ├── kmeans_compression.py
│   ├── pca_compression.py
│   ├── svd_compression.py
│   ├── metrics.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Image-Compression-Studio.git
```

Navigate to the project directory:

```bash
cd Image-Compression-Studio
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Learning Outcomes

This project demonstrates practical applications of:

* Image Processing
* Clustering Algorithms
* Dimensionality Reduction
* Compression Techniques
* Streamlit Application Development
* Image Quality Evaluation

---

## Author

**Athira Suresh**

Developed as an educational project to explore and compare image compression techniques through interactive visualization and quantitative evaluation.
