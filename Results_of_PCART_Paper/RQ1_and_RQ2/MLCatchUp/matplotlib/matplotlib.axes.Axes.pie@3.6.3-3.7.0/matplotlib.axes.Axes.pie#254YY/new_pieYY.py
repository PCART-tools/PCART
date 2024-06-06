import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, pctdistance=0.6, labels=['A', 'B', 'C', 'D'], colors=None, radius=1, startangle=90, autopct='%1.1f%%', explode=None, shadow=False, normalize=True, labeldistance=1.1, hatch=None)
