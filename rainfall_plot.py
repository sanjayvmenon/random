import csv
import matplotlib.pyplot as plt

# Update this path to the actual location of your CSV file
file_path = '/Users/sanjayvmenon/plotproject/bangalore-rainfall-data-1900-2024-sept.csv'

years = []
rainfall = []

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row

    for row in reader:
        try:
            # Check if the first column is numeric and convert it
            year = int(row[0])  # Assuming the first column is 'Year'
            rainfall_amount = float(row[1])  # Assuming the second column is 'Rainfall'
            
            years.append(year)
            rainfall.append(rainfall_amount)

        except ValueError as e:
            print(f"Skipping row due to error: {e}. Row data: {row}")

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(years, rainfall, marker='o', linestyle='-', color='b')

# Add labels and title
plt.title('Bangalore Rainfall (1900-2024)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Rainfall (mm)', fontsize=12)

# Display the plot
plt.grid(True)
plt.show()