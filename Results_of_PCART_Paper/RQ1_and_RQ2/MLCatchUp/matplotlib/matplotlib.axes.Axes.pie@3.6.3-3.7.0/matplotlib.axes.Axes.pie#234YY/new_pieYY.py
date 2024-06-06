import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', 0.6, radius=1, normalize=True, labeldistance=1.1, shadow=False, startangle=90, hatch=None)
