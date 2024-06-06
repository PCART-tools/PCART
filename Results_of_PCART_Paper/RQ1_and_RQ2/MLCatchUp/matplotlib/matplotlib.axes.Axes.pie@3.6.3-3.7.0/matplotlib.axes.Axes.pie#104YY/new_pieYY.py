import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, pctdistance=0.6, autopct='%1.1f%%', normalize=True, colors=None, labels=['A', 'B', 'C', 'D'], data=None, explode=None, hatch=None)
