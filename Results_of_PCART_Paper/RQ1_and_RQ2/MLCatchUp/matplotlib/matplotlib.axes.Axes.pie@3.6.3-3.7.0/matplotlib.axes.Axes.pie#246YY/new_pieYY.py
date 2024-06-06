import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], labeldistance=1.1, shadow=False, startangle=90, autopct='%1.1f%%', normalize=True, radius=1, pctdistance=0.6, colors=None, hatch=None)
