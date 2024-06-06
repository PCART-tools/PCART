import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(autopct='%1.1f%%', explode=None, x=x, labeldistance=1.1, pctdistance=0.6, normalize=True, startangle=90, colors=None, shadow=False, labels=['A', 'B', 'C', 'D'], hatch=None)
