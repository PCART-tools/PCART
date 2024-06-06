import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', pctdistance=0.6, counterclock=True, shadow=False, labeldistance=1.1, radius=1, normalize=True, startangle=90, hatch=None)
