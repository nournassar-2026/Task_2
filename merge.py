import pandas as pd
import numpy as np

# Load data
df_1 = pd.read_csv('Task_2_data/researchers.csv')
df_2 = pd.read_json('Task_2_data/publications.json')
df_3 = pd.read_excel('Task_2_data/funding.xlsx')

# Inner merge (keeps only matching records)
merged_inner = pd.merge(df_1, df_2, on='researcher_id', how='inner')
merged_inner = pd.merge(merged_inner, df_3, on='researcher_id', how='inner')

# Left merge (keeps all researchers, even without publications or funding)
merged_left = pd.merge(df_1, df_2, on='researcher_id', how='left')
merged_left = pd.merge(merged_left, df_3, on='researcher_id', how='left')

# Print shapes for comparison
print("Inner merge shape:", merged_inner.shape)
print("Left merge shape:", merged_left.shape)