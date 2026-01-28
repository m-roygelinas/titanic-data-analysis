import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("titanic.csv")

# -----------------------------------------------------------------------------
# Get basic info about the dataframe
# -----------------------------------------------------------------------------

print(df.head())  
print(df.info())

# -----------------------------------------------------------------------------
# Basic statistics
# -----------------------------------------------------------------------------

survivors_by_class = df.groupby('Pclass')['Survived'].sum()
#print("Survivors by Class:\n", survivors_by_class)

survivors_by_sex = df.groupby('Sex')['Survived'].sum()
#print("Survivors by Sex:\n", survivors_by_sex)

survivors_by_age = df.groupby("Age")['Survived'].sum()
#print("Survivors by Age:\n", survivors_by_age)

# -----------------------------------------------------------------------------
# Analyze survival rates by age groups -> create age groups
# -----------------------------------------------------------------------------

# Replace \N with NaN
df['Age'] = df['Age'].replace('\\N', np.nan)

# Ensure Age column is numeric and deals with errors by converting invalid parsing to NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Drop rows with missing age values
if df['Age'].isna().sum() != 0:
    df_clean = df.dropna(subset=['Age'])
else:
    df_clean = df.copy()