# Create sample DataFrame with missing values
import pandas as pd
import numpy as np
from src.eda_dolphin.components.missing import check_missing
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [1, 2, 3, 4, 5],
    'C': [np.nan, np.nan, 3, 4, np.nan],
    'D': ['x', 'y', np.nan, 'z', 'w']
}

df = pd.DataFrame(data)

# Use the function
result = check_missing(df)
print(result)