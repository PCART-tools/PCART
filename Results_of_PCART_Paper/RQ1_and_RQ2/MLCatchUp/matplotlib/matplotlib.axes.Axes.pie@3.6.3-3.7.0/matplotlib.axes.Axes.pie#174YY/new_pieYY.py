import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(labels=['A', 'B', 'C', 'D'], labeldistance=1.1, autopct='%1.1f%%', x=x, pctdistance=0.6, explode=None, colors=None, normalize=True, shadow=False, hatch=None)
