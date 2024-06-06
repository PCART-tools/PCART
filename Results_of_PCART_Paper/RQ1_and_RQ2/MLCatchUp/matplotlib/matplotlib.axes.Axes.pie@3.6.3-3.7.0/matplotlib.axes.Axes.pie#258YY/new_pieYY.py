import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(pctdistance=0.6, explode=None, shadow=False, x=x, radius=1, normalize=True, autopct='%1.1f%%', colors=None, labeldistance=1.1, startangle=90, labels=['A', 'B', 'C', 'D'], hatch=None)
