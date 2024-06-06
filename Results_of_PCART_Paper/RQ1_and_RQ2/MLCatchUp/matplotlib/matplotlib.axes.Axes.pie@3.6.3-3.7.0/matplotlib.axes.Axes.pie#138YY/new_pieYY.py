import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x=x, pctdistance=0.6, autopct='%1.1f%%', normalize=True, explode=None, labels=['A', 'B', 'C', 'D'], colors=None, shadow=False, hatch=None)
