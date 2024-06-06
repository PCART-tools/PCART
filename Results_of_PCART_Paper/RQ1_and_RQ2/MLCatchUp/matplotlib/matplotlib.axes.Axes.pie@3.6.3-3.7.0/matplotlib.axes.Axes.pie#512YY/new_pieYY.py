import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', 0.6, False, normalize=True, frame=False, counterclock=True, startangle=90, center=(0, 0), wedgeprops=None, data=None, textprops=None, labeldistance=1.1, radius=1, hatch=None)
