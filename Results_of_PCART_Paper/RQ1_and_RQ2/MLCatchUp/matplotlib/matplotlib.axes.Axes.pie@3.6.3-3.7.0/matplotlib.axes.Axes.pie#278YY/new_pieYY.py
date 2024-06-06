import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', 0.6, False, startangle=90, normalize=True, counterclock=True, labeldistance=1.1, radius=1, hatch=None)
