import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("cleaned_student_data.csv")

# Display First 5 Rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
df.info()

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Correlation Matrix
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# Histogram - Math Score
plt.figure(figsize=(6, 4))
plt.hist(df["MathScore"], bins=10)
plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")
plt.savefig("Histogram.png")
plt.show()

# Bar Chart - Average Scores
average_scores = df[["MathScore", "ScienceScore"]].mean()

plt.figure(figsize=(6, 4))
average_scores.plot(kind="bar")
plt.title("Average Scores")
plt.ylabel("Average Marks")
plt.savefig("BarChart.png")
plt.show()

# Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(data=df[["MathScore", "ScienceScore"]])
plt.title("Box Plot of Scores")
plt.savefig("BoxPlot.png")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("Correlation_Heatmap.png")
plt.show()

print("\nEDA Completed Successfully.")
