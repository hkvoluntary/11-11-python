import pandas as pd

# Load the first Excel sheet into a DataFrame
df1 = pd.read_excel('output.xlsx')

# Load the second Excel sheet into a DataFrame
df2 = pd.read_excel('output1.xlsx')

# Merge the two DataFrames on the common column 'Id'
merged_df = pd.merge(df1, df2, on='Id')

# Save the merged DataFrame to a new Excel file
merged_df.to_excel('merged_output.xlsx', index=False)

print("Data has been merged and saved to merged_output.xlsx")
