import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import dotenv_values
import pandas as pd
import numpy as np

variables = dotenv_values(".env")

file = variables["FILE"]

df = pd.read_csv(file)

co = df.at[0, 'co']
no = df.at[0, 'no']
no2 = df.at[0, 'no2']
o3 = df.at[0, 'o3']
so2 = df.at[0, 'so2']
pm2_5 = df.at[0, 'pm2_5']
pm10 = df.at[0, 'pm10']
nh3 = df.at[0, 'nh3']

values = [co, no, no2, o3, so2, pm2_5, pm10, nh3]

colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(values)))

# plot
fig, ax = plt.subplots()
ax.pie(values, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)


plt.show()