import pandas as pd

# Load data from a CSV file
df = pd.read_csv('data.csv')

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nDataset Information:")
print(df.info())

# Calculate basic statistics for numerical columns
print("\nStatistics of numerical columns:")
print(df.describe())

# Filter data where a specific column meets a condition
filtered_df = df[df['column_name'] > 50]
print("\nRows where 'column_name' is greater than 50:")
print(filtered_df)