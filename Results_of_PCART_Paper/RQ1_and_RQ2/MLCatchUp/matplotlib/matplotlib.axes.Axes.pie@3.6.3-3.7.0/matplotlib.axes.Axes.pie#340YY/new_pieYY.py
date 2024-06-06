import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', pctdistance=0.6, counterclock=True, radius=1, startangle=90, normalize=True, wedgeprops=None, data=None, labeldistance=1.1, shadow=False, hatch=None)
