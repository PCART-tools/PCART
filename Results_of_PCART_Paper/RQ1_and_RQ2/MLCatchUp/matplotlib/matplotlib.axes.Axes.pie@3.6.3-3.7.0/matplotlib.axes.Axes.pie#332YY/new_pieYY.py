import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', 0.6, False, normalize=True, startangle=90, counterclock=True, wedgeprops=None, radius=1, data=None, labeldistance=1.1, hatch=None)
