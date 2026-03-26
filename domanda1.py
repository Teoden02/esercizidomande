import pandas as pd

# Load your dataset
df = pd.read_csv('food-inspection.csv')  # Adjust file path/format as needed

# Check the columns available
print(df.columns)
print(df.head())

# Count activity types and find the most common
activity_counts = df['activity_type'].value_counts()  # Adjust column name as needed
print(activity_counts)

# Get the most checked activity
most_checked = activity_counts.idxmax()
print(f"Most checked activity: {most_checked}")