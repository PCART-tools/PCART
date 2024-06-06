import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], None, normalize=True, shadow=False, pctdistance=0.6, counterclock=True, labeldistance=1.1, autopct='%1.1f%%', radius=1, startangle=90, hatch=None)
