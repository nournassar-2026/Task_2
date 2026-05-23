import pandas as pd
import numpy as np
import os

# Run merge
exec(open('merge.py').read())

# Run clean
exec(open('clean.py').read())

# Researcher with highest citations
max_citations_row = clean_inner.loc[clean_inner['citations'].idxmax()]
print(f"\nResearcher with highest citations:")
print(f"Name: {max_citations_row['first_name']} {max_citations_row['last_name']}")
print(f"Citations: {max_citations_row['citations']}")

# Field with most funding
funding_by_field = clean_inner.groupby('field')['amount_cad'].sum()
print(f"\nField with most funding:")
print(f"{funding_by_field.idxmax()}: ${funding_by_field.max():,.2f}")

# Earliest joined active researcher
active = clean_inner[clean_inner['is_active'] == True]
earliest = active.loc[active['joined_year'].idxmin()]
print(f"\nEarliest joined active researcher:")
print(f"Name: {earliest['first_name']} {earliest['last_name']}")
print(f"Year: {earliest['joined_year']}")

# Save both versions
os.makedirs('output', exist_ok=True)
clean_inner.to_csv('output/clean_research_data_inner.csv', index=False)

print("FILE SAVED:")
print("output/clean_research_data_inner.csv")

