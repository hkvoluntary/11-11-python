import pandas as pd

# Sample data
#data = [
#    {"Id": 1, "Name": "Alice", "Age": 28},
#    {"Id": 2, "Name": "Bob", "Age": 34},
#    {"Id": 3, "Name": "Charlie", "Age": 22}
#]

data = [
    {"Id": 1, "Department": "IT"},
    {"Id": 2, "Department": "HR"},
    {"Id": 3, "Department": "Sales"}
]

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to Excel file
df.to_excel("output1.xlsx", index=False)

print("Data has been saved to output1.xlsx")
