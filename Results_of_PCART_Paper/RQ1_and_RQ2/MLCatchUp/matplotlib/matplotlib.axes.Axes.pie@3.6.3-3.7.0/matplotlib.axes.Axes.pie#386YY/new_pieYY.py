import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', 0.6, False, normalize=True, radius=1, labeldistance=1.1, startangle=90, counterclock=True, textprops=None, wedgeprops=None, hatch=None)
