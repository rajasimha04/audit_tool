import pandas as pd
import re

# Load CSV or Excel
file_path = "sample_data.csv"
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

# Initialize issues report
report = []

# Check for missing values
missing = df.isnull().sum()
report.append("Missing Values:\n" + str(missing))

# Check for duplicates
duplicates = df.duplicated().sum()
report.append(f"Duplicate Rows: {duplicates}")

# Check date format
def is_valid_date(date_str):
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", str(date_str)))

invalid_dates = df['Date of Birth'].apply(lambda x: not is_valid_date(x)).sum()
report.append(f"Invalid Date Format in 'Date of Birth': {invalid_dates}")

# Save report
with open("data_quality_report.txt", "w") as f:
    f.write("\n\n".join(report))

print("✅ Data quality audit completed. See 'data_quality_report.txt'")
