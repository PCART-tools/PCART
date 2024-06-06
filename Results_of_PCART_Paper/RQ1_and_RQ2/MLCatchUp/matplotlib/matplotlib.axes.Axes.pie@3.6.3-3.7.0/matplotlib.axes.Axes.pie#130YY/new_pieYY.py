import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, shadow=False, normalize=True, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%', colors=None, pctdistance=0.6, hatch=None)
