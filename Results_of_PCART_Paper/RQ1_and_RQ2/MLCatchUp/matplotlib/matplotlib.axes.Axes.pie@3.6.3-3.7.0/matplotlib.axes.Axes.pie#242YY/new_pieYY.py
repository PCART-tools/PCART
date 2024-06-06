import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, labeldistance=1.1, pctdistance=0.6, autopct='%1.1f%%', normalize=True, startangle=90, radius=1, shadow=False, hatch=None)
