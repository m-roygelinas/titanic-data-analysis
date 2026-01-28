import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("titanic.csv")

print(df.head())  
print(df.info())