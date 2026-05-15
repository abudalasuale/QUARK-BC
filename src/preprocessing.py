"""Data preprocessing and cleaning pipeline."""

import numpy as np
import pandas as pd
from typing import Tuple, Optional, Dict
from sklearn.preprocessing import StandardScaler, LabelEncoder


class DataPreprocessor:
    """Data preprocessing and cleaning pipeline for breast cancer data.
    
    Attributes:
        scaler: StandardScaler instance for normalization
        encoders: Dictionary of LabelEncoders for categorical variables
    """

    def __init__(self):
        """Initialize the DataPreprocessor."""
        self.scaler = StandardScaler()
        self.encoders = {}

    def load_data(self, filepath: str) -> pd.DataFrame:
        """Load data from CSV file.
        
        Args:
            filepath: Path to CSV file
            
        Returns:
            Loaded DataFrame
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is empty
        """
        try:
            df = pd.read_csv(filepath)
            if df.empty:
                raise ValueError("CSV file is empty")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")

    def check_data_quality(self, df: pd.DataFrame) -> Dict:
        """Check data quality and return statistics.
        
        Args:
            df: Input DataFrame
            
        Returns:
            Dictionary with data quality metrics
        """
        return {
            "shape": df.shape,
            "missing_values": df.isnull().sum().to_dict(),
            "missing_percent": (df.isnull().sum() / len(df) * 100).to_dict(),
            "dtypes": df.dtypes.to_dict(),
            "duplicates": df.duplicated().sum(),
            "memory_usage": df.memory_usage(deep=True).sum() / 1024 ** 2,  # MB
        }

    def handle_missing_values(
        self, df: pd.DataFrame, method: str = "mean"
    ) -> pd.DataFrame:
        """Handle missing values in the DataFrame.
        
        Args:
            df: Input DataFrame
            method: Strategy for handling missing values.
                    Options: 'mean', 'median', 'drop', 'forward_fill'
                    Default: 'mean'
                    
        Returns:
            DataFrame with handled missing values
            
        Raises:
            ValueError: If method is not recognized
        """
        df = df.copy()
        
        if method == "mean":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        elif method == "median":
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        elif method == "drop":
            df = df.dropna()
        elif method == "forward_fill":
            df = df.fillna(method="ffill")
        else:
            raise ValueError(f"Unknown method: {method}")
        
        return df

    def remove_outliers(
        self, df: pd.DataFrame, method: str = "iqr", threshold: float = 1.5
    ) -> pd.DataFrame:
        """Remove outliers from numerical columns.
        
        Args:
            df: Input DataFrame
            method: Strategy for outlier detection.
                    Options: 'iqr', 'zscore'
                    Default: 'iqr'
            threshold: Threshold for outlier detection.
                       For IQR: multiplier (default 1.5)
                       For Z-score: standard deviations (default 1.5)
                       
        Returns:
            DataFrame without outliers
            
        Raises:
            ValueError: If method is not recognized
        """
        df = df.copy()
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        if method == "iqr":
            Q1 = df[numeric_cols].quantile(0.25)
            Q3 = df[numeric_cols].quantile(0.75)
            IQR = Q3 - Q1
            mask = ~((df[numeric_cols] < (Q1 - threshold * IQR)) |
                     (df[numeric_cols] > (Q3 + threshold * IQR))).any(axis=1)
            df = df[mask]
        elif method == "zscore":
            from scipy import stats
            z_scores = np.abs(stats.zscore(df[numeric_cols].fillna(df[numeric_cols].mean())))
            mask = (z_scores < threshold).all(axis=1)
            df = df[mask]
        else:
            raise ValueError(f"Unknown method: {method}")
        
        return df

    def encode_categorical(self, df: pd.DataFrame) -> pd.DataFrame:
        """Encode categorical variables.
        
        Args:
            df: Input DataFrame
            
        Returns:
            DataFrame with encoded categorical variables
        """
        df = df.copy()
        categorical_cols = df.select_dtypes(include=["object"]).columns
        
        for col in categorical_cols:
            if col not in self.encoders:
                self.encoders[col] = LabelEncoder()
                df[col] = self.encoders[col].fit_transform(df[col].astype(str))
            else:
                df[col] = self.encoders[col].transform(df[col].astype(str))
        
        return df

    def normalize_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalize numerical features using z-score normalization.
        
        Args:
            df: Input DataFrame
            
        Returns:
            DataFrame with normalized features
        """
        df = df.copy()
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        return df

    def preprocess_pipeline(
        self,
        df: pd.DataFrame,
        target_col: str,
        handle_missing: str = "mean",
        remove_outliers: bool = True,
        remove_outliers_method: str = "iqr",
        encode_categorical: bool = True,
        normalize: bool = True,
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Complete preprocessing pipeline.
        
        Args:
            df: Input DataFrame
            target_col: Name of target column
            handle_missing: Strategy for missing values. Default: 'mean'
            remove_outliers: Whether to remove outliers. Default: True
            remove_outliers_method: Outlier detection method. Default: 'iqr'
            encode_categorical: Whether to encode categorical vars. Default: True
            normalize: Whether to normalize features. Default: True
            
        Returns:
            Tuple of (features, labels) as numpy arrays
            
        Raises:
            ValueError: If target_col is not in DataFrame
        """
        if target_col not in df.columns:
            raise ValueError(f"Target column '{target_col}' not found in DataFrame")
        
        # Check quality
        quality = self.check_data_quality(df)
        print(f"Initial data shape: {quality['shape']}")
        print(f"Missing values: {quality['missing_values']}")
        
        # Handle missing values
        df = self.handle_missing_values(df, method=handle_missing)
        print(f"After handling missing values: {df.shape}")
        
        # Remove outliers
        if remove_outliers:
            df = self.remove_outliers(df, method=remove_outliers_method)
            print(f"After removing outliers: {df.shape}")
        
        # Separate features and target
        X = df.drop(columns=[target_col])
        y = df[target_col]
        
        # Encode categorical variables
        if encode_categorical:
            X = self.encode_categorical(X)
        
        # Normalize features
        if normalize:
            X = self.normalize_features(X)
        
        print(f"Final features shape: {X.shape}")
        print(f"Final labels shape: {y.shape}")
        
        return X.values, y.values
