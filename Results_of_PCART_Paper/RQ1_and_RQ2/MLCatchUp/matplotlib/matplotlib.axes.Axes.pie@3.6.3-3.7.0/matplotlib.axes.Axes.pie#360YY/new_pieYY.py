import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(labels=['A', 'B', 'C', 'D'], shadow=False, startangle=90, autopct='%1.1f%%', explode=None, radius=1, wedgeprops=None, colors=None, normalize=True, data=None, counterclock=True, labeldistance=1.1, pctdistance=0.6, x=x, hatch=None)
