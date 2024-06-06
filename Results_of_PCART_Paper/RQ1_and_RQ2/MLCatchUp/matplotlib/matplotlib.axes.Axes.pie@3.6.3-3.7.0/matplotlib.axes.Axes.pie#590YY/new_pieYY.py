import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, rotatelabels=False, normalize=True, labeldistance=1.1, textprops=None, center=(0, 0), radius=1, startangle=90, counterclock=True, pctdistance=0.6, wedgeprops=None, shadow=False, frame=False, autopct='%1.1f%%', hatch=None)
