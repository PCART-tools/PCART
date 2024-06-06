import matplotlib.pyplot as plt
x = [45, 25, 15, 15]
plt.pie(x, None, ['A', 'B', 'C', 'D'], autopct='%1.1f%%', pctdistance=0.6, normalize=True, radius=1, counterclock=True, shadow=False, labeldistance=1.1, colors=None, startangle=90, wedgeprops=None, hatch=None)
