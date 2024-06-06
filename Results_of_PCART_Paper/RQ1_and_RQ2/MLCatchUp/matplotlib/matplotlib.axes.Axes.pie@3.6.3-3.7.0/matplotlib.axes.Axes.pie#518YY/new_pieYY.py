import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, '%1.1f%%', labeldistance=1.1, normalize=True, pctdistance=0.6, shadow=False, startangle=90, center=(0, 0), radius=1, counterclock=True, wedgeprops=None, frame=False, textprops=None, hatch=None)
