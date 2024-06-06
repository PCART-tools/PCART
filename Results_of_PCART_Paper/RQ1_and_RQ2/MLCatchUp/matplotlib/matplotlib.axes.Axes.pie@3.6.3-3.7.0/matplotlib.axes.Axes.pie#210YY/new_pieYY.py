import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, pctdistance=0.6, labeldistance=1.1, explode=None, labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%', normalize=True, shadow=False, colors=None, startangle=90, hatch=None)
