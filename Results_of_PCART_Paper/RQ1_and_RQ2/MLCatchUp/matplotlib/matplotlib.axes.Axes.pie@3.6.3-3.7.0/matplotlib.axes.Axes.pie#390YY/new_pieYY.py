import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', 0.6, counterclock=True, shadow=False, normalize=True, labeldistance=1.1, wedgeprops=None, startangle=90, radius=1, textprops=None, hatch=None)
