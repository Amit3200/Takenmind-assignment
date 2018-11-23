import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
exf=pd.ExcelFile("f2m.xlsx")
df=exf.parse('f2m_ratios')
#print(df)
df1=df.groupby(["Age","Year"],as_index=False).sum()
#print(df1)
dfu=df1.pivot("Age","Year","Ratio")
dfu.reset_index()
flat=pd.DataFrame(dfu.to_records())
print(flat["Age"])
df1i=flat[:]
del df1i["Age"]
pd.isnull(np.array(df1i, dtype=float))
print(df1i)
plt.figure(figsize=(8,8))
ax=sns.heatmap(df1i,fmt="g", linewidths=.5,yticklabels=flat["Age"],cmap="plasma")
plt.title("Year vs Age - Sex Ratio")
plt.ylabel("Age Range")
plt.xlabel("Year")
plt.savefig("Save2.png")
plt.show()
