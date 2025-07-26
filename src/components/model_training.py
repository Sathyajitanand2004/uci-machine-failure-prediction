import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier
)
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                # Linear Models
                'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
                # Tree-based Models
                'Random Forest': RandomForestClassifier(random_state=42, n_estimators=100),
                'Extra Trees': ExtraTreesClassifier(random_state=42, n_estimators=100),
                'Decision Tree': DecisionTreeClassifier(random_state=42),
                'Gradient Boosting': GradientBoostingClassifier(random_state=42),
                'AdaBoost': AdaBoostClassifier(random_state=42),
                'XGBoost': XGBClassifier(random_state=42, eval_metric='logloss'),
                # Instance-based Models
                'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=5),
                # Probabilistic Models
                'Naive Bayes': GaussianNB(),
                # Support Vector Machines
                'Support Vector Machine': SVC(random_state=42, probability=True),
            }

            params = {
                'Random Forest': {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [None, 10, 20, 30],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                },
                'XGBoost': {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [3, 5, 7],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'subsample': [0.8, 0.9, 1.0]
                },
                'Gradient Boosting': {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 0.2],
                    'max_depth': [3, 5, 7],
                    'subsample': [0.8, 0.9, 1.0]
                },
                'Support Vector Machine': {
                    'C': [0.1, 1, 10, 100],
                    'gamma': ['scale', 'auto', 0.1, 1],
                    'kernel': ['rbf', 'linear']
                },
                'Logistic Regression': {
                    'C': [0.1, 1, 10, 100],
                    'penalty': ['l1', 'l2'],
                    'solver': ['liblinear', 'saga']
                },
                'Decision Tree': {
                    'criterion': ['gini', 'entropy', 'log_loss'],
                    'max_depth': [None, 5, 10, 20],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4],
                    'max_features': [None, 'sqrt', 'log2']
                },
                # Add empty dictionaries for models without hyperparameters to tune
                'Extra Trees': {},
                'AdaBoost': {},
                'K-Nearest Neighbors': {},
                'Naive Bayes': {}
            }

            # Modified to return both scores and fitted models
            model_report, fitted_models = evaluate_models(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                models=models, param=params
            )

            # To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            # Get the fitted model instead of the original unfitted one
            best_model = fitted_models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found", sys)
            
            logging.info(f"Best found model on both training and testing dataset: {best_model_name} with score: {best_model_score}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            # Now the model is already fitted, so we can predict directly
            predicted = best_model.predict(X_test)
            accuracy = accuracy_score(y_test, predicted)
            
            return accuracy

        except Exception as e:
            raise CustomException(e, sys)