import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, autopct='%1.1f%%', shadow=False, normalize=True, pctdistance=0.6, labeldistance=1.1, hatch=None)
