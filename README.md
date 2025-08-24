# EDA Dolphin

**EDA Dolphin** is a lightweight Python library for performing **Exploratory Data Analysis (EDA)** quickly and efficiently.  
It provides easy-to-use functions for data loading, missing values analysis, statistical summaries, and visualization.

---

## Features

- Load datasets from CSV files
- Generate summary statistics of datasets
- Check for missing values and create missing value reports
- Plot histograms and other visualizations easily
- Modular and easy to extend

---

## Installation

You can install dependencies via `pip` or `conda`:

```bash
# Using pip
pip install EDA_Dolphin

# Using conda
conda install EDA_Dolphin


### `check_missing(df)`

Check missing values in a pandas DataFrame.

**Parameters:**
- `df` (`pandas.DataFrame`): Input dataset

**Returns:**
- `pandas.Series`: Count of missing values for each column

**Example:**

```python
import pandas as pd
from eda_dolphin import check_missing

data = {
    "A": [1, 2, None, 4],
    "B": [None, 2, 3, 4]
}

df = pd.DataFrame(data)

print(check_missing(df))
