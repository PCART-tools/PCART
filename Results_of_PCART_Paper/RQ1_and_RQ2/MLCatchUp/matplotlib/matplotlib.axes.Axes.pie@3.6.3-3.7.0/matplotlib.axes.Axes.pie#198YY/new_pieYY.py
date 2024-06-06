import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, startangle=90, autopct='%1.1f%%', pctdistance=0.6, normalize=True, shadow=False, labeldistance=1.1, hatch=None)
