import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "Telco_customer_churn.xlsx"

df = pd.read_excel(DATA_PATH)
print(df.shape)

print("=" * 50)

columns_to_drop = [
    "CustomerID",
    "Count",
    "Country",
    "State",
    "City",
    "Zip Code",
    "Lat Long",
    "Latitude",
    "Longitude",
    "Churn Value",
    "Churn Score",
    "Churn Reason"
]

df = df.drop(columns=columns_to_drop)
print(df.columns)

print("=" * 50)

df["Total Charges"] = pd.to_numeric(
    df["Total Charges"],
    errors="coerce"
)

print(df["Total Charges"].dtype)
print("=" * 50)
print(df.isnull().sum())

df = df.dropna()
print("After dropping missing values:")
print(df.shape)

# preprocess target column
print("=" * 50)
df["Churn Label"] = df["Churn Label"].map({
    "No":0,
    "Yes":1
})

print(df["Churn Label"].value_counts())

print("=" * 50)
# verify the data types of the columns
print(df.info())
print(df.head())
print(df.isnull().sum())


#prepare the features and target variable

x= df.drop(columns=["Churn Label"])
y= df["Churn Label"]

print("=" * 50)
print(x.shape)  
print(y.shape)



# identify categorical and numerical features

categorical_features = x.select_dtypes(include=["object"]).columns.tolist()

numerical_features = x.select_dtypes(
    include=["int64", "float64"]
).columns.tolist()

print(categorical_features)
print(numerical_features)

#now we process thhem using columnTransformer


# bulid the preprocessor using ColumnTransformer and Pipeline

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler


preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_features
        ),
        #df = pd.get_dummies(df) It works, 
        #but it's not suitable for deployment because when a new category appears in production, 
        # your model can break.
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ]
)


# now we split the data into train and test sets

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)


x_train_processed = preprocessor.fit_transform(x_train)
x_test_processed = preprocessor.transform(x_test)


print(x_train_processed.shape)
print(x_test_processed.shape)

print(y_train.shape)
print(y_test.shape)

# now we save the preprocessor object to a file using joblib

from pathlib import Path
from joblib import dump

# Parent directory of the current file
BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(exist_ok=True)

dump(preprocessor, MODELS_DIR / "preprocessor.pkl")