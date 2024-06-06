import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], pctdistance=0.6, colors=None, normalize=True, shadow=False, radius=1, labeldistance=1.1, counterclock=True, autopct='%1.1f%%', startangle=90, hatch=None)
