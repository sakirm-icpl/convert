import pandas as pd
import json
import os
 
# Specify the JSON file name
json_file_name = "/var/lib/jenkins/workspace/test/insecure-bank-Reference.json"
 
# Extract the base name of the JSON file (without extension)
base_name = os.path.splitext(os.path.basename(json_file_name))[0]
 
# Load JSON data from file
with open(json_file_name, 'r') as json_file:
    data = json.load(json_file)
 
# Convert JSON to DataFrame
df = pd.json_normalize(data)
 
# Save DataFrame to Excel with the same base name as JSON file
excel_file_name = f'{base_name}.xlsx'
df.to_excel(excel_file_name, index=False)
 
print(f"Conversion completed. Excel file saved as: {excel_file_name}")
