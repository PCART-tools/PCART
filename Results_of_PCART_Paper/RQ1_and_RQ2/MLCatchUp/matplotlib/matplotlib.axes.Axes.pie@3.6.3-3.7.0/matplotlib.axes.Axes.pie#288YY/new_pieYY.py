import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', labeldistance=1.1, shadow=False, radius=1, counterclock=True, startangle=90, pctdistance=0.6, normalize=True, data=None, hatch=None)
