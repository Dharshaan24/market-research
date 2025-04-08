import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\downloads\\archive\\allo-doc-PHCS_2017.csv")

# Standardize column names (remove spaces & convert to lowercase)
df.columns = df.columns.str.strip().str.lower()

# Print column names to verify correct names
print("Column Names in Dataset:", df.columns)

# Rename columns if necessary (use actual column names from print(df.columns))
df.rename(columns={'state_name': 'state', 'doctor_shortfall': 'doctor shortfall'}, inplace=True)

# Check if 'state' and 'doctor shortfall' exist
if 'state' not in df.columns or 'doctor shortfall' not in df.columns:
    raise ValueError("Column names do not match. Check dataset and update column names.")

# Ensure 'doctor shortfall' column is numeric
df['doctor shortfall'] = pd.to_numeric(df['doctor shortfall'], errors='coerce')

# Drop NaN values (if any) to avoid errors in plotting
df = df.dropna(subset=['doctor shortfall'])

# Sort values for better visualization
df = df.sort_values(by='doctor shortfall', ascending=False)

# Plot doctor shortages across states
plt.figure(figsize=(12, 6))
sns.barplot(x='state', y='doctor shortfall', data=df, palette='coolwarm')
plt.xticks(rotation=90)
plt.xlabel("State")
plt.ylabel("Doctor Shortfall")
plt.title("Doctor Shortages Across States")
plt.show()
