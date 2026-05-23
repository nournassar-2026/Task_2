import pandas as pd
import numpy as np

# Clean inner merge
clean_inner = merged_inner.copy()
clean_inner['amount_cad'] = clean_inner['amount_cad'].clip(lower=0)
clean_inner = clean_inner.dropna()

# Clean left merge
clean_left = merged_left.copy()
clean_left['amount_cad'] = clean_left['amount_cad'].clip(lower=0)
clean_left = clean_left.dropna()

print("\nInner clean shape:", clean_inner.shape)
print("Left clean shape:", clean_left.shape)