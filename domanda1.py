import pandas as pd
from collections import Counter

# Load your inspection data (adjust file path and format as needed)
df = pd.read_csv('./archivio/food-inspections.csv')

# Example with sample data structure
# Assuming your data has a 'facility_type' column
df = pd.read_csv('./archivio/food-inspections.csv')

# Count inspections by facility type
inspection_counts = df['Facility Type'].value_counts()

# Print results
print(inspection_counts)

# Or if using a list/dictionary:
#most_common = Counter(establishment_types).most_common(10)
# for est_type, count in most_common:
#     print(f"{est_type}: {count} inspections")