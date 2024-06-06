import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, labeldistance=1.1, pctdistance=0.6, shadow=False, radius=1, counterclock=True, colors=None, autopct='%1.1f%%', startangle=90, labels=['A', 'B', 'C', 'D'], wedgeprops=None, explode=None, normalize=True, hatch=None)
