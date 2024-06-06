import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(pctdistance=0.6, explode=None, startangle=90, x=x, autopct='%1.1f%%', shadow=False, counterclock=True, normalize=True, labeldistance=1.1, labels=['A', 'B', 'C', 'D'], colors=None, radius=1, hatch=None)
