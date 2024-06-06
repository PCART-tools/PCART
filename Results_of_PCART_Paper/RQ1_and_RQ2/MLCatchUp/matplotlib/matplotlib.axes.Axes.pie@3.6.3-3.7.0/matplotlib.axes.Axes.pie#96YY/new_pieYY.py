import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], autopct='%1.1f%%', normalize=True, pctdistance=0.6, colors=None, data=None, hatch=None)
