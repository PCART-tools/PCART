import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, autopct='%1.1f%%', pctdistance=0.6, normalize=True, shadow=False, data=None, colors=None, labels=['A', 'B', 'C', 'D'], labeldistance=1.1, hatch=None)
