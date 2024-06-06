import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, labeldistance=1.1, normalize=True, labels=['A', 'B', 'C', 'D'], explode=None, pctdistance=0.6, startangle=90, radius=1, counterclock=True, shadow=False, autopct='%1.1f%%', colors=None, hatch=None)
