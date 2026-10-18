"""Contrast enhancement: CLAHE and Single-Scale Retinex.

Part of the GTAU (large-animal eye diagnostics) image-processing work.
Functions are intentionally dependency-light: numpy + opencv-python.
"""

import cv2
import numpy as np


def apply_clahe(gray: np.ndarray, clip_limit: float = 2.0, tile_grid: tuple = (8, 8)) -> np.ndarray:
    """Apply CLAHE to a grayscale image.

    Args:
        gray: 2D uint8 grayscale image.
        clip_limit: contrast clipping limit (higher = stronger enhancement).
        tile_grid: grid size for local histogram equalization.
    """
    if gray.ndim != 2:
        raise ValueError("apply_clahe expects a 2D grayscale image")
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid)
    return clahe.apply(gray)


def single_scale_retinex(img: np.ndarray, sigma: float = 15.0) -> np.ndarray:
    """Single-Scale Retinex for illumination normalization.

    Estimates illumination with a Gaussian blur and recovers reflectance
    in log space: R = log(I) - log(I * G_sigma).

    Args:
        img: grayscale or BGR uint8 image.
        sigma: Gaussian sigma for the illumination estimate.
    """
    img_f = img.astype(np.float32) + 1.0
    if img_f.ndim == 3:
        blur = cv2.GaussianBlur(img_f, (0, 0), sigma)
    else:
        blur = cv2.GaussianBlur(img_f, (0, 0), sigma)
    retinex = np.log(img_f) - np.log(blur + 1.0)
    # Normalize to 0-255 for display
    retinex -= retinex.min()
    if retinex.max() > 0:
        retinex = retinex / retinex.max()
    return (retinex * 255).astype(np.uint8)


def to_grayscale(img: np.ndarray) -> np.ndarray:
    """Convert BGR image to grayscale; pass through if already grayscale."""
    if img.ndim == 2:
        return img
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def compare_methods(img: np.ndarray) -> dict:
    """Run all enhancement methods and return a dict of named results."""
    gray = to_grayscale(img)
    return {
        "original": gray,
        "clahe": apply_clahe(gray),
        "retinex": single_scale_retinex(gray),
    }
