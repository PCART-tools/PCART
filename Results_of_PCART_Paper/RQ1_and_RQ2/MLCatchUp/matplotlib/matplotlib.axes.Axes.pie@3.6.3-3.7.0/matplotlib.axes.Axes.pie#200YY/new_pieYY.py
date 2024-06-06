import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, normalize=True, startangle=90, pctdistance=0.6, data=None, autopct='%1.1f%%', shadow=False, labeldistance=1.1, hatch=None)
