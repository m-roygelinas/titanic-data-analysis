import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from pathlib import Path

# Get the directory of the current script, then go up one level to data
data_path = Path(__file__).parent.parent / "data" / "titanic.csv"
df = pd.read_csv(data_path)

# -----------------------------------------------------------------------------
# Get basic info about the dataframe
# -----------------------------------------------------------------------------

print(df.head())  
print(df.info())
print("Number of duplicated rows:", df[df.duplicated()].shape[0])

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
# Function to get counts and survival rate
# -----------------------------------------------------------------------------

def get_counts_and_rate_of_survivors(grouped_df):
    result = grouped_df.agg(
        total_survived = ('Survived', 'sum'),
        total_count = ('Survived', 'count')
    )
    result['survival_percentage'] = (
        (grouped_df['Survived'].mean() * 100)
        .round(0)
        .astype(int)
        .astype(str) + '%'
    )
    return result

# -----------------------------------------------------------------------------
# Analyze survival rates by age groups and plot graph
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

# calculate percentage of missing values in Age column
missing_age_percentage = (df['Age'].isna().sum() / len(df)) * 100
print(f"Percentage of missing values in Age column: {missing_age_percentage:.2f}%")

# Define bin edges and labels
bins = [0, 18, 30, 45, 55, 65, float('inf')]
labels = ['0-18', '19-30', '31-45', '46-55', '56-65', '66+']

# Create age_group column
df_clean['age_group'] = pd.cut(df_clean['Age'], bins=bins, labels=labels, right=True)

# Group survivors by age group
survivors_by_age_groups = df_clean.groupby('age_group')[['Survived']].sum()

# Get counts and survival rate by age group
survivors_by_age_and_count = get_counts_and_rate_of_survivors(
    df_clean.groupby('age_group')
    )

print(survivors_by_age_and_count)

# Pie charts of survivors by age group
labels = ['Deaths', 'Survivors']
configure = dict(labels=labels, 
             autopct='%1.1f%%', # Display percentages on each slice
             shadow=True,
             explode=[0, 0.1])  # Explode the second slice
fig, ax = plt.subplots(2, 3, figsize=(12, 8))  # Create a 2x3 grid of subplots

survivors = survivors_by_age_and_count.loc['0-18', 'total_survived']
deaths = survivors_by_age_and_count.loc['0-18', 'total_count'] - survivors
ax[0, 0].pie([deaths, survivors], **configure)
ax[0,0].set_title('0-18')

survivors = survivors_by_age_and_count.loc['19-30', 'total_survived']
deaths = survivors_by_age_and_count.loc['19-30', 'total_count'] - survivors
ax[0, 1].pie([deaths, survivors], **configure)
ax[0,1].set_title('19-30')

survivors = survivors_by_age_and_count.loc['31-45', 'total_survived']
deaths = survivors_by_age_and_count.loc['31-45', 'total_count'] - survivors
ax[0, 2].pie([deaths, survivors], **configure)
ax[0,2].set_title('31-45')

survivors = survivors_by_age_and_count.loc['46-55', 'total_survived']
deaths = survivors_by_age_and_count.loc['46-55', 'total_count'] - survivors
ax[1, 0].pie([deaths, survivors], **configure)
ax[1,0].set_title('46-55')
survivors = survivors_by_age_and_count.loc['56-65', 'total_survived']
deaths = survivors_by_age_and_count.loc['56-65', 'total_count'] - survivors
ax[1, 1].pie([deaths, survivors], **configure)
ax[1,1].set_title('56-65')

survivors = survivors_by_age_and_count.loc['66+', 'total_survived']
deaths = survivors_by_age_and_count.loc['66+', 'total_count'] - survivors
ax[1, 2].pie([deaths, survivors], **configure)
ax[1,2].set_title('66+')

plt.suptitle('Survivors by Age Group')
plt.show()

# Bar chart of survivors by age group
plt.bar(
    x=survivors_by_age_and_count.index,
    height=survivors_by_age_and_count['total_survived']
    )
plt.xlabel('Age Group')
plt.ylabel('Number of Survivors')
plt.title('Survivors by Age Group')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Histogram of age groups
plt.hist(df_clean['age_group'].sort_values(), bins=6)  # Create a histogram with 6 bins
plt.xlabel('Age Group')
plt.ylabel('Number of Survivors')
plt.title('Distribution of Number of Survivors by Age Group')
plt.show()

# -----------------------------------------------------------------------------
# Get counts and survival rate by sex and plot graph
# -----------------------------------------------------------------------------

# Get counts and survival rate by sex
survivors_by_sex_and_count = get_counts_and_rate_of_survivors(
    df.groupby('Sex')
    )
print(survivors_by_sex_and_count)

# Bar chart of survivors by sex
plt.bar(
    x=survivors_by_sex_and_count.index,
    height=survivors_by_sex_and_count['total_survived']
    )
plt.xlabel('Sex')
plt.ylabel('Number of Survivors')
plt.title('Survivors by Sex')
plt.tight_layout()
plt.show()

# Pie chart of survivors by sex
labels = ['Female', 'Male']
sizes = survivors_by_sex_and_count['total_survived']
plt.pie(sizes, labels=labels, 
        autopct='%1.1f%%', # Display percentages on each slice
        shadow=True,
        explode=[0, 0.1])  # Explode the second slice
plt.title('Survivors by Sex')
plt.show()

# -----------------------------------------------------------------------------
# Get counts and survival rate by class and plot graph
# -----------------------------------------------------------------------------

# Get counts and survival rate by class
survivors_by_class_and_count = get_counts_and_rate_of_survivors(
    df.groupby('Pclass')
    )
print(survivors_by_class_and_count)

# Bar chart of survival percentage by class
plt.bar(
    x=survivors_by_class_and_count.index,
    height=survivors_by_class_and_count['survival_percentage'].str.rstrip('%').astype(int)
    )
plt.xlabel('Class')
plt.ylabel('Percentage of Survivors')
plt.title('Percentage of Survivors by Class')
plt.xticks(np.arange(0, 4, 1))
plt.tight_layout()
plt.show()