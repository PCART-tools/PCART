import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, autopct='%1.1f%%', normalize=True, labeldistance=1.1, labels=['A', 'B', 'C', 'D'], colors=None, shadow=False, pctdistance=0.6, explode=None, hatch=None)
