import pandas as pd

# Define the dataset path
dataset_path = "C:/Users/USER/Nox_share/Download/Medical report/asthma-emergency-department-visit-rates-by-county-2015_2019.csv"

# Load the dataset using pandas
df = pd.read_csv(dataset_path, encoding='latin1')

# Display the values in the dataset
print(df.head())

# Generate a basic report
report = {}

# Count the number of rows in the dataset
report["Total Rows"] = len(df)

# Count the number of columns in the dataset
report["Total Columns"] = len(df.columns)

# Calculate the average value of the "NUMBER OF ED VISITS" column
df["NUMBER OF ED VISITS"] = pd.to_numeric(df["NUMBER OF ED VISITS"], errors='coerce')
report["Average ED Visits"] = df["NUMBER OF ED VISITS"].fillna(0).mean()

# Display the report
print("\nReport:")
for key, value in report.items():
    print(f"{key}: {value}")
