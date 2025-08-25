import pandas as pd
import numpy as np
from src.eda_dolphin.components.missing import  check_missing

df = pd.read_csv("data.csv")

result = check_missing(df)
print(result)
