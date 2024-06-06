import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, normalize=True, pctdistance=0.6, colors=None, shadow=False, autopct='%1.1f%%', labeldistance=1.1, labels=['A', 'B', 'C', 'D'], hatch=None)
