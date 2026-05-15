"""Breast Cancer Prediction Model using Random Forest."""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, Optional, Any
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
)


class BreastCancerModel:
    """Machine Learning model for breast cancer phenotype prediction.
    
    Uses Random Forest Classifier to predict breast cancer phenotypes
    with special focus on Triple-Negative Breast Cancer (TNBC).
    
    Attributes:
        model: RandomForestClassifier instance
        X_train: Training features
        X_test: Testing features
        y_train: Training labels
        y_test: Testing labels
        metrics: Dictionary of performance metrics
    """

    def __init__(
        self,
        n_estimators: int = 100,
        random_state: int = 42,
        max_depth: Optional[int] = None,
        min_samples_split: int = 2,
    ):
        """Initialize the Breast Cancer Model.
        
        Args:
            n_estimators: Number of trees in the forest. Default: 100
            random_state: Random seed for reproducibility. Default: 42
            max_depth: Maximum depth of trees. Default: None (unlimited)
            min_samples_split: Minimum samples to split a node. Default: 2
        """
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            random_state=random_state,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            n_jobs=-1,
        )
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.metrics = {}
        self.feature_names = None

    def train(
        self,
        X: np.ndarray,
        y: np.ndarray,
        test_size: float = 0.2,
        cv: int = 5,
    ) -> Dict[str, float]:
        """Train the model with cross-validation.
        
        Args:
            X: Training features (n_samples, n_features)
            y: Training labels (n_samples,)
            test_size: Proportion of data for testing. Default: 0.2
            cv: Number of cross-validation folds. Default: 5
            
        Returns:
            Dictionary with performance metrics
            
        Raises:
            ValueError: If X or y are empty or have mismatched sizes
        """
        if X.size == 0 or y.size == 0:
            raise ValueError("X and y cannot be empty")
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must have the same number of samples")

        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y
        )

        # Train model
        self.model.fit(self.X_train, self.y_train)

        # Cross-validation
        cv_scores = cross_validate(
            self.model,
            self.X_train,
            self.y_train,
            cv=cv,
            scoring=["accuracy", "precision_weighted", "recall_weighted", "f1_weighted"],
        )

        # Get predictions
        y_pred_train = self.model.predict(self.X_train)
        y_pred_test = self.model.predict(self.X_test)
        y_pred_proba = self.model.predict_proba(self.X_test)

        # Calculate metrics
        self.metrics = {
            "train_accuracy": accuracy_score(self.y_train, y_pred_train),
            "test_accuracy": accuracy_score(self.y_test, y_pred_test),
            "precision": precision_score(self.y_test, y_pred_test, average="weighted", zero_division=0),
            "recall": recall_score(self.y_test, y_pred_test, average="weighted", zero_division=0),
            "f1": f1_score(self.y_test, y_pred_test, average="weighted", zero_division=0),
            "cv_accuracy_mean": cv_scores["test_accuracy"].mean(),
            "cv_accuracy_std": cv_scores["test_accuracy"].std(),
        }

        # Add ROC-AUC if binary or multiclass
        if len(np.unique(y)) == 2:
            self.metrics["roc_auc"] = roc_auc_score(self.y_test, y_pred_proba[:, 1])
        else:
            self.metrics["roc_auc"] = roc_auc_score(
                self.y_test, y_pred_proba, multi_class="ovr", average="weighted"
            )

        return self.metrics

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions on new data.
        
        Args:
            X: Features (n_samples, n_features)
            
        Returns:
            Predicted class labels (n_samples,)
            
        Raises:
            ValueError: If model hasn't been trained yet
        """
        if self.model.classes_ is None:
            raise ValueError("Model must be trained before making predictions")
        return self.model.predict(X)

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """Get prediction probabilities.
        
        Args:
            X: Features (n_samples, n_features)
            
        Returns:
            Probability predictions (n_samples, n_classes)
        """
        if self.model.classes_ is None:
            raise ValueError("Model must be trained before making predictions")
        return self.model.predict_proba(X)

    def get_feature_importance(self) -> pd.DataFrame:
        """Get feature importance scores.
        
        Returns:
            DataFrame with feature importance ranked
        """
        importances = self.model.feature_importances_
        feature_names = self.feature_names or [f"Feature {i}" for i in range(len(importances))]
        
        df = pd.DataFrame(
            {"feature": feature_names, "importance": importances}
        ).sort_values("importance", ascending=False)
        
        return df

    def get_confusion_matrix(self) -> np.ndarray:
        """Get confusion matrix on test set.
        
        Returns:
            Confusion matrix
        """
        if self.X_test is None:
            raise ValueError("Model must be trained first")
        y_pred = self.model.predict(self.X_test)
        return confusion_matrix(self.y_test, y_pred)

    def get_model_info(self) -> Dict[str, Any]:
        """Get model information and metrics.
        
        Returns:
            Dictionary with model info and metrics
        """
        return {
            "model_type": "Random Forest Classifier",
            "n_estimators": self.model.n_estimators,
            "max_depth": self.model.max_depth,
            "n_features": self.model.n_features_in_ if hasattr(self.model, "n_features_in_") else None,
            "n_classes": len(self.model.classes_) if hasattr(self.model, "classes_") else None,
            "metrics": self.metrics,
        }

    def set_feature_names(self, names: list) -> None:
        """Set feature names for better interpretability.
        
        Args:
            names: List of feature names
        """
        self.feature_names = names
