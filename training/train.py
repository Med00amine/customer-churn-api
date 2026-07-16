import os
import joblib
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from preprocess import *
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

rf = RandomForestClassifier(
    n_estimators=500,
    criterion="gini",
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features="sqrt",
    bootstrap=True,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1,
    oob_score=True
)

# prepare the data for training and testing
model = Pipeline([
    ("preprocessor", preprocessor),
    (
        "classifier", rf
    )
])

# now we fit the model to the training data
model.fit(
    x_train,
    y_train
)

# now we make predictions on the test data
predictions = model.predict(x_test)

probabilities = model.predict_proba(x_test)[:,1]   
 

# now we evaluate the model using various metrics
print("="*50)
print("Accuracy")
print("="*50)

print(
    accuracy_score(
        y_test,
        predictions
    )
)

print("="*50)
print("Precision")
print("="*50)

print(
    precision_score(
        y_test,
        predictions
    )
)

print("="*50)
print("Recall")
print("="*50)

print(
    recall_score(
        y_test,
        predictions
    )
)

print("="*50)
print("F1")
print("="*50)

print(
    f1_score(
        y_test,
        predictions
    )
)

print("="*50)
print("ROC AUC")
print("="*50)

print(
    roc_auc_score(
        y_test,
        probabilities
    )
)

# print the classification report

print(
    classification_report(
        y_test,
        predictions
    )
)

# print the confusion matrix
print(
    confusion_matrix(
        y_test,
        predictions
    )
)



# now we save the preprocessor object to a file using joblib

from pathlib import Path
from joblib import dump

# Parent directory of the current file
BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(exist_ok=True)

dump(model, MODELS_DIR / "RandomForest_Model.pkl")
print(f"Model saved to {MODELS_DIR}/RandomForest_Model.pkl")