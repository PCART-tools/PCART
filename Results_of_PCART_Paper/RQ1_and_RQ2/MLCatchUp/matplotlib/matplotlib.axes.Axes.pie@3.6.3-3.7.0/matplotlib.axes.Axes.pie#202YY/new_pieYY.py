import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], pctdistance=0.6, labeldistance=1.1, autopct='%1.1f%%', shadow=False, normalize=True, colors=None, startangle=90, hatch=None)
