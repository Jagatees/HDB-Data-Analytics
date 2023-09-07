import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('ProjTest\Excel Data\Test Data.csv', header=None)
df.head()
Xaxis = df[0]
Yaxis = df[1]

fig, ax = plt.subplots(figsize=(10,7))
ax.bar(Xaxis,Yaxis)
ax.set_xlabel('Name',fontsize=14)
ax.set_ylabel('Salary',fontsize=14)
ax.set_title('Test Graph',fontsize=14)
plt.show()