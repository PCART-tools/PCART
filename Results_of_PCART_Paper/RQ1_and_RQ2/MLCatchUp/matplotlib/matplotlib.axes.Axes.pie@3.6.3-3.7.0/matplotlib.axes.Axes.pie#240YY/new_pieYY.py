import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', labeldistance=1.1, startangle=90, pctdistance=0.6, shadow=False, normalize=True, data=None, radius=1, hatch=None)
