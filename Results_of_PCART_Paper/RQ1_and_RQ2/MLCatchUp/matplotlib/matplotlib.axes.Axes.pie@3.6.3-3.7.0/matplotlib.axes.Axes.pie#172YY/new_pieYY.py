import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, normalize=True, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%', labeldistance=1.1, explode=None, pctdistance=0.6, colors=None, data=None, shadow=False, hatch=None)
