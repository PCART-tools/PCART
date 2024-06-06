import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], pctdistance=0.6, normalize=True, colors=None, autopct='%1.1f%%', radius=1, labeldistance=1.1, textprops=None, wedgeprops=None, counterclock=True, startangle=90, data=None, shadow=False, hatch=None)
