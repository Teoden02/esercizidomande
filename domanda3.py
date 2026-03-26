import pandas as pd

# Load your data
df = pd.read_csv('archivio/food-inspections.csv')

# Distribution of inspection outcomes by risk category
# 'distribution' is a DataFrame showing the count of each inspection outcome for every risk category.
distribution = df.groupby(['risk_category', 'inspection_outcome']).size().unstack(fill_value=0)

# Display results
print(distribution)

# Optional: Calculate percentages
distribution_percentage = distribution.div(distribution.sum(axis=1), axis=0) * 100
print(distribution_percentage)

# Optional: Visualize with matplotlib
import matplotlib.pyplot as plt
distribution.plot(kind='bar', figsize=(12, 6))
plt.title('Distribution of Inspection Outcomes by Risk Category')
plt.xlabel('Risk Category')
plt.ylabel('Count')
plt.legend(title='Outcome')
plt.tight_layout()
plt.show()