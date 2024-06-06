import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', shadow=False, radius=1, normalize=True, wedgeprops=None, labeldistance=1.1, startangle=90, counterclock=True, pctdistance=0.6, hatch=None)
