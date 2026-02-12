import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("data/sales.csv")

print("Initial Data:")
print(df)

# 2. Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# 3. Fill missing values
df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].median())
df["PurchaseAmount"] = df["PurchaseAmount"].fillna(df["PurchaseAmount"].mean())


print("\nAfter Cleaning:")
print(df.isnull().sum())

# 4. Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# 5. Average purchase by city
city_avg = df.groupby("City")["PurchaseAmount"].mean()
print("\nAverage Purchase by City:")
print(city_avg)

# 6. Visualization
plt.hist(df["PurchaseAmount"], bins=5)
plt.title("Purchase Amount Distribution")
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.show()
