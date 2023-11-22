import pandas as pd
import json

# Load JSON file
with open('/var/lib/jenkins/workspace/MobSF/Reference.json') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.json_normalize(data)

# Save to Excel
df.to_excel('/var/lib/jenkins/workspace/mobsf/Reference.xlsx', index=False)
