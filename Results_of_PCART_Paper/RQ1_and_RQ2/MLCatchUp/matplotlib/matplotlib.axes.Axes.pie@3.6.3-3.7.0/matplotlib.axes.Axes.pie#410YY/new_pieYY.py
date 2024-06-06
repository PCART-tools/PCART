import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, shadow=False, counterclock=True, autopct='%1.1f%%', textprops=None, radius=1, explode=None, colors=None, labeldistance=1.1, normalize=True, startangle=90, pctdistance=0.6, wedgeprops=None, labels=['A', 'B', 'C', 'D'], hatch=None)
