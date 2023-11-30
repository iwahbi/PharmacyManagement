# create_csv.py

import pandas as pd

# Sample user-drug interaction data
data = {
    'user_id': [1, 1, 2, 2, 3],
    'drug_id': [101, 102, 101, 103, 102],
    'rating': [5, 4, 3, 2, 5],
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('pharam.csv', index=False)

print('CSV file created successfully.')

