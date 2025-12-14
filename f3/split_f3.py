import pandas as pd
import numpy as np
import re

df = pd.read_csv("/home/ali.lawati/dia-guard/inputs/F3_Consistency.csv")
url_pattern = r'https?://\S+|www\.\S+'

# Apply the regex to the 'text_column' to remove URLs
# The `flags=re.IGNORECASE` makes the matching case-insensitive.
df['human_content'] = df['human_content'].str.replace(url_pattern, '', regex=True, flags=re.IGNORECASE)
df['ai_content'] = df['ai_content'].str.replace(url_pattern, '', regex=True, flags=re.IGNORECASE)

# Optional: Remove any extra whitespace that might be left after removing URLs
df['human_content'] = df['human_content'].str.strip().str.replace(r'\s+', ' ', regex=True)
df['ai_content'] = df['ai_content'].str.strip().str.replace(r'\s+', ' ', regex=True)


num_files = 10
total_rows = len(df)
rows_per_file = total_rows // num_files
remainder = total_rows % num_files

start_index = 0
for i in range(num_files):
    end_index = start_index + rows_per_file
    if i < remainder:  # Distribute the remainder rows among the first 'remainder' files
        end_index += 1


    chunk_df = df.iloc[start_index:end_index]
    
    # Save the chunk to a CSV file
    file_name = f"f3_{i+1}.csv"
    chunk_df.to_csv(file_name, index=False) 
    print(f"Saved {len(chunk_df)} rows to {file_name}")
    
    start_index = end_index