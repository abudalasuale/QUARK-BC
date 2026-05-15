"""QUARK-BC - Breast Cancer Prediction Model

A Machine Learning project for predicting breast cancer phenotypes,
with special focus on Triple-Negative Breast Cancer (TNBC).
"""

__version__ = "1.0.0"
__author__ = "Abudala Sualé"
__email__ = "abudala@example.com"

from .model import BreastCancerModel
from .preprocessing import DataPreprocessor

__all__ = [
    "BreastCancerModel",
    "DataPreprocessor",
]
