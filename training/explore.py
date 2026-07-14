import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_excel(f"D:\Amine\github\customer-churn-api\data\Telco_customer_churn.xlsx")

# ==========================
# Basic Information
# ==========================

print("=" * 50)
print("First 5 rows")
print("=" * 50)
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nCategorical Summary:")
print(df.describe(include="object"))

print("\nClass imbalanced:")
print(df["Churn Value"].value_counts())
print(df["Churn Value"].value_counts(normalize=True) * 100)


print("\nMissing Values heatmap:")
sns.heatmap(df.isnull(), cbar=False)
plt.show()

#numerical distribution
num_cols = [
    "Tenure Months",
    "Monthly Charges",
]

for col in num_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col], kde=True)
    plt.title(col)
    plt.show()
# ==========================
# Target Distribution
# ==========================

plt.figure(figsize=(6,4))
x="Churn Value"
sns.countplot(data=df, x=x)

plt.title("Customer Churn Distribution")
plt.tight_layout()
plt.show()

print("\nTarget Distribution")

print(df["Churn Value"].value_counts())

print("\nTarget Percentage")

print(df["Churn Value"].value_counts(normalize=True) * 100)