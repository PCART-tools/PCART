import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], pctdistance=0.6, shadow=False, normalize=True, startangle=90, data=None, colors=None, labeldistance=1.1, autopct='%1.1f%%', hatch=None)
