# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# 1. Display first 5 and last 5 rows
print("Top 5 rows of the dataset:")
print(df.head())
print("\nLast 5 rows of the dataset:")
print(df.tail())

# 2. Descriptive statistics
print("\nDescriptive statistics of the dataset:")
print(df.describe())

# 3. Number of independent and dependent variables
print("\nTotal columns (variables):", df.shape[1])
print("Dependent Variable: Survived")
print("Independent Variables:", list(df.columns.drop('Survived')))

# 4. Independent variable with minimum average
print("\nAverage of independent variables:")
print(df.mean(numeric_only=True))
print("\nVariable with minimum average value:")
print(df.mean(numeric_only=True).idxmin())

# 5. Variable with highest standard deviation
print("\nVariable with highest standard deviation:")
print(df.std(numeric_only=True).idxmax())

# 6. Missing values in each column
print("\nMissing values in each column:")
print(df.isnull().sum())

# 7. Visualizing missing values
sns.heatmap(df.isnull(), cbar=False, cmap="YlOrRd")
plt.title("Missing Values Heatmap")
plt.show()

# 8. Column with max missing values
print("\nColumn with maximum missing values:")
print(df.isnull().sum().idxmax())

# 9. Replacing missing values in 'Age' with average
avg_age = df['Age'].mean()
df['Age'].fillna(avg_age, inplace=True)
print("\nMissing values in 'Age' column after filling:", df['Age'].isnull().sum())

# 10. Histogram for Age distribution
plt.hist(df['Age'], bins=20, color='skyblue', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 11. Outliers using Boxplot
plt.boxplot(df['Fare'])
plt.title("Boxplot of Fare")
plt.ylabel("Fare")
plt.show()
print("\n'Fare' has outliers as seen in the boxplot.")

# 12. Line chart to show Fare trend
plt.plot(df['Fare'].head(50))
plt.title("Fare Trend")
plt.xlabel("Passenger Index")
plt.ylabel("Fare")
plt.show()

# 13. Correlation Matrix
corr = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr)

# Strong positive and negative correlation
print("\nStrongest Positive Correlation:", corr.unstack().sort_values(ascending=False)[1])
print("Strongest Negative Correlation:", corr.unstack().sort_values()[0])

# 14. Scatter plots
plt.scatter(df['Fare'], df['Survived'], alpha=0.5)
plt.title("Fare vs Survived")
plt.xlabel("Fare")
plt.ylabel("Survived")
plt.show()

plt.scatter(df['Age'], df['Survived'], alpha=0.5)
plt.title("Age vs Survived")
plt.xlabel("Age")
plt.ylabel("Survived")
plt.show()
