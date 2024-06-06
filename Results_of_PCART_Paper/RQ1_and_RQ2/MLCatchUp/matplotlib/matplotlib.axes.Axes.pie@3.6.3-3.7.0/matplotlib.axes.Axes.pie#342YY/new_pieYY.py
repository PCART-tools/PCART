import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, normalize=True, counterclock=True, wedgeprops=None, startangle=90, radius=1, autopct='%1.1f%%', shadow=False, labeldistance=1.1, pctdistance=0.6, hatch=None)
