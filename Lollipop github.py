#Libraries
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#Import data
home = pd.read_csv("home.csv")
away = pd.read_csv("away.csv")
#Reverse order
home = home.iloc[::-1]
away = away.iloc[::-1]

plt.figure(figsize = (9, 6))
sns.set_style("whitegrid", {'grid.linestyle': '--'})
my_range=range(1,len(home.index)+1)

ax = plt.axes(frameon=False)
plt.hlines(y=my_range, xmin=home['Pts'], xmax=away['Pts'], color='#8f9c9a', lw =2)
plt.scatter(home['Pts'], my_range, color='#003953', s=75, label='Home', zorder=3)
plt.scatter(away['Pts'], my_range, color='#0096d7', s=75, label='Away', zorder=3)


plt.legend(ncol=2, bbox_to_anchor=(1., 1.01), loc="lower right", frameon=False)
plt.yticks(my_range, home['Squad'])
plt.title("Home vs Away points", loc='left', fontsize=14)
plt.xlabel('Points')
plt.tight_layout()

plt.savefig("Lollypop.png")
plt.show()
plt.close()
