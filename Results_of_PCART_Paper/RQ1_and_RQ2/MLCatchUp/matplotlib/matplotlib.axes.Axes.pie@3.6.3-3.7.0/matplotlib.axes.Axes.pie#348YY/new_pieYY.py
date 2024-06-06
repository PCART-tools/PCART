import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], autopct='%1.1f%%', startangle=90, normalize=True, labeldistance=1.1, counterclock=True, radius=1, wedgeprops=None, pctdistance=0.6, colors=None, data=None, shadow=False, hatch=None)
