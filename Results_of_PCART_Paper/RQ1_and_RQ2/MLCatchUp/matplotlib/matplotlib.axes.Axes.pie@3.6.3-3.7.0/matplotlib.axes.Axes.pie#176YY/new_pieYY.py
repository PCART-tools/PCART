import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(autopct='%1.1f%%', labeldistance=1.1, explode=None, x=x, normalize=True, labels=['A', 'B', 'C', 'D'], data=None, colors=None, shadow=False, pctdistance=0.6, hatch=None)
