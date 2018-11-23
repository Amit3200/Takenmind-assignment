import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
exf=pd.ExcelFile("f2m.xlsx")
df=exf.parse('xh')
df1=df[:]
del df1["Age"]
pd.isnull(np.array(df1, dtype=float))
cols=df.columns
plt.figure(figsize=(9,9))
ax=sns.heatmap(df1,fmt="g", linewidths=.5,yticklabels=df["Age"],cmap="plasma")
plt.title("Year vs Age - Sex Ratio")
plt.ylabel("Age Range")
plt.xlabel("Year")
plt.savefig("Save1.png")
plt.show()
